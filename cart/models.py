from django.db import models
from custom_caps.models import Caps
from user.models import CustomUser


#Модель корзины.
# user: прописал юзера наследуется от Кастомюзера.
# item_caps: вторым полем идет обращающение к самому модели кепки,
# quantity_caps: количество товара.
# created_at: дата время создания товара.
#updated_at: дата и время обновления
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Пользователь")
    item_caps = models.ForeignKey(Caps, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Товар")
    quantity_caps = models.IntegerField(null=False, verbose_name="Количество кепок")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано в")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено в")

    def __str__(self):
        return f'ID {self.id}: {self.item_caps}'


#Модель стоимости доставки.
# status: статус доставки (активный, пассивныый).
# cost_of_delivery_caps: цена доставки товара.
# cost_of_caps: цена самого товара.
# fixed_price: фиксированная цена
# created_at: дата время создания товара.
#updated_at: дата и время обновления товара
class DeliveryCost(models.Model):
    STATUS_CHOICES = (
        ('Active', 'active'),
        ('Passive', 'passive')
    )
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default="passive", null=False, verbose_name="Статус")
    cost_of_delivery_caps = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Стоимость доставки кепок")
    cost_of_caps = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Стоимость кепок")
    fixed_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Фиксированная цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано в")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено в")

    def __str__(self):
        return f'ID {self.id}: {self.status}: {self.cost_of_caps}'
