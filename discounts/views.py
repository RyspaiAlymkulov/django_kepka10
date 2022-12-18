from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import MagazineCoupon, MagazineDiscount
from .serializers import MagazineDiscountSerializer, MagazineCouponSerializer


class MagazineDiscountListAPIview(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, ]
    queryset = MagazineDiscount.objects.all().order_by('id')
    serializer_class = MagazineDiscountSerializer


class MagazineCouponListAPIview(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, ]
    queryset = MagazineCoupon.objects.all().order_by('id')
    serializer_class = MagazineCouponSerializer
