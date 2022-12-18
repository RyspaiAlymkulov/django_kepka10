from rest_framework import serializers
from custom_caps.models import Magazine, Manufacturer, Caps, UserCapsRelation, Category


class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'


class ManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    magazine = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='magazine-detail')

    class Meta:
        model = Manufacturer
        fields = '__all__'


class CapsSerializer(serializers.HyperlinkedModelSerializer):
    likes_count = serializers.SerializerMethodField()
    magazine = serializers.SlugRelatedField(
        queryset=Magazine.objects.all(), slug_field='name')
    manufacturer = serializers.SlugRelatedField(
        queryset=Manufacturer.objects.all(), slug_field='name')
    currency = serializers.ChoiceField(
        choices=Caps.CURRENCY_CHOICES)
    currency_name = serializers.CharField(
        source='get_currency_display',
        read_only=True)

    class Meta:
        model = Caps
        fields = '__all__'

    def get_likes_count(self, instance):
        return UserCapsRelation.objects.filter(book=instance, like=True).count()


class UserCapsRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCapsRelation
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'created_at', 'updated_at']