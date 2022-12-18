from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import serializers
from user.models import CustomUser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class CustomUserSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField()
    phone = serializers.CharField()
    regions = serializers.CharField()
    image = serializers.ImageField()

    class Meta:
        model = CustomUser
        fields = [
            'name', 'id', 'first_name', 'email', 'password', 'phone', 'regions', 'image'
        ]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['phone', 'email', 'username', 'password']

    def validate(self, attrs):
        phone = attrs.get('phone_number', '')
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('Имя пользователя должно содержать только буквенно цифровые символы!')
        return attrs

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, read_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = CustomUser.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = CustomUser
        fields = ['phone', 'email', 'password', 'username', 'tokens']


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    # redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('Ссылка сброса недействительна', 401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed('Ссылка сброса недействительна', 401)
        return super().validate(attrs)


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=30)
    last_name = serializers.DateField()
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=15)
    region = serializers.CharField(max_length=15)
    address = serializers.CharField(max_length=255)
    image = serializers.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = [
            "username", "name", "last_name", "email",
            "region", "address", "image", "phone_number"
        ]


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_message = {
        'bad_token': ('Токен просрочен или недействителен')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')