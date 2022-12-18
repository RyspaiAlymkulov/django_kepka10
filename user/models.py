from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, username, password, phone, **extra_fields):
        if not email:
            raise ValueError("Пожалуйста введите номер телефона")
        if not email:
            raise ValueError("Пожалуйста введите Емейл")
        if not username:
            raise ValueError("Пожалуйста введите Логин")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password, phone):
        return self._create_user(email, username, password, phone)

    def create_superuser(self, email, username, password, phone):
        return self._create_user(
            email, username, password, phone, is_staff=True, is_superuser=True
        )


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True, db_index=True)
    name = models.CharField(verbose_name="Имя", max_length=255)
    last_name = models.CharField(verbose_name="Фамилия", max_length=255)
    email = models.EmailField(verbose_name="Почта пользователя",
                              max_length=255, unique=True, db_index=True)
    regions = models.CharField(max_length=150, verbose_name='Регион')
    address = models.TextField(default='прописать адрес проживания... ')
    image = models.ImageField(verbose_name='Фотография пользователя', null=True, blank=True)
    phone = PhoneNumberField(max_length=50, verbose_name='Номер телефона', unique=True)
    password = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(
        max_length=255, blank=False,
        null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
