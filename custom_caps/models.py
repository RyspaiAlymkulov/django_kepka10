from user.models import CustomUser
from django.db import models


class Magazine(models.Model):
    title = models.TextField(default='default', verbose_name="Заглавие")
    name = models.CharField(max_length=60, verbose_name="Название")
    description = models.TextField(default='default', verbose_name="Описание")
    image = models.ImageField(null=True, blank=True, verbose_name="Фотография")
    publication_date = models.DateTimeField(auto_now=True, verbose_name="Дата создания")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'ID {self.id}: {self.name}'


class Category(models.Model):
    title = models.CharField(max_length=255, null=False, verbose_name="Заглавие")
    category_id = models.IntegerField(null=True, blank=True, verbose_name="ID-Категории")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано в")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено в")

    def __str__(self):
        return f'ID {self.id}: {self.title}'


class Manufacturer(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    country_of_origin = models.CharField(blank=True, null=True, max_length=50, verbose_name="Страна производства")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'ID {self.id}: {self.name}'


class Caps(models.Model):
    CURRENCY_CHOICES = (
        ('USD', 'DOLLAR'),
        ('KGS', 'SOM'),
        ('TENGE', 'TENGE'),
    )
    SIZE_CHOICES = (
        ('Small', 'S'),
        ('Medium', 'M'),
        ('Large', 'L'),
        ('eXtra Large', 'XL')
    )
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    buyer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, verbose_name="Покупатель")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name="Категория")
    size = models.CharField(choices=SIZE_CHOICES, max_length=30, verbose_name="Размер")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(null=True, blank=True, verbose_name="Фотография")
    magazine = models.ForeignKey(Magazine,
                                 related_name='Shops',
                                 on_delete=models.CASCADE, verbose_name="Магазин")
    manufacturer = models.ForeignKey(Manufacturer,
                                     related_name='Shops',
                                     on_delete=models.CASCADE, verbose_name="Производитель")
    currency = models.CharField(max_length=100, choices=CURRENCY_CHOICES,
                                default='kgz', verbose_name="Валюта")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано в")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено в")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'ID {self.id}: {self.name}'


class UserCapsRelation(models.Model):
    RATING_CHOICES = (
        (1,  'Нормально'),
        (2, 'Хорошо'),
        (3, 'Отлично'),
        (4, 'Прекрасно'),
        (5, 'Изумительно')
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    caps = models.ForeignKey(Caps, on_delete=models.CASCADE, verbose_name="Кепка")
    like = models.BooleanField(default=False, verbose_name="Нравится")
    favorites = models.BooleanField(default=False, verbose_name="Избранное")
    rate = models.PositiveSmallIntegerField(choices=RATING_CHOICES, null=True, verbose_name="Оценка")

    def __str__(self):
        return f'ID {self.id}: {self.user}: {self.caps.name}'