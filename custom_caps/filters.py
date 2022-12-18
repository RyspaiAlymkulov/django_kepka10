import django_filters
from .models import Caps


class CapsFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    size = django_filters.CharFilter(name='size', lookup_expr='icontains')
    manufacturer = django_filters.NumberFilter(name='manufacturer')
    category = django_filters.NumberFilter(name='category')
    price = django_filters.NumberFilter(name='price')
    created_at = django_filters.NumberFilter(name='created_at')
    updated_at = django_filters.NumberFilter(name='updated_at')

    class Meta:
        model = Caps
        fields = ['name', 'size', 'manufacturer', 'category',
                  'price', 'created_at', 'updated_at', ]
