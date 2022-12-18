from discounts.models import MagazineDiscount, MagazineCoupon
from rest_framework import serializers


class MagazineDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineDiscount
        fields = ['id', 'discount_type', 'discount_rate', 'discount_amount', 'minimum_purchased_items',
                  'apply_to', 'target_caps', 'target_category', 'created_at', 'updated_at']


class MagazineCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazineCoupon
        fields = ['id', 'minimum_cart_amount', 'discount_rate_caps', 'created_at', 'updated_at']