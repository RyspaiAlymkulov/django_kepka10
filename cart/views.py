from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import CustomUser
from .models import Cart, DeliveryCost
from .serializers import UserCartSerializer, CartSerializer, DeliveryCostSerializer


class UserListAPIview(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, ]
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserCartSerializer


class CartListAPIview(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all().order_by('id')
    serializer_class = CartSerializer


class DeliveryListAPIview(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, ]
    queryset = DeliveryCost.objects.all().order_by('id')
    serializer_class = DeliveryCostSerializer
