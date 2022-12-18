from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from custom_caps.filters import CapsFilter
from custom_caps.models import Magazine, Manufacturer, Caps, UserCapsRelation, Category
from custom_caps.serializers import MagazineSerializer, ManufacturerSerializer, CapsSerializer, \
    UserCapsRelationSerializer, CategorySerializer
from rest_framework import generics, filters
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .pagination import CapsPagination


class MagazineListAPIview(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    pagination_class = PageNumberPagination
    authentication_classes = [JWTAuthentication, ]
    name = 'magazine-list'


class MagazineItemUpdateDeleteAPIview(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    authentication_classes = [JWTAuthentication, ]
    name = 'magazine-detail'
    lookup_field = 'id'


class ManufacturerListAPIview(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    pagination_class = PageNumberPagination
    authentication_classes = [JWTAuthentication, ]
    name = 'manufacturer-list'


class ManufacturerItemUpdateDeleteAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, ]
    name = 'manufacturer-detail'
    lookup_field = 'id'


class CapsListAPIview(viewsets.ModelViewSet):
    queryset = Caps.objects.all()
    serializer_class = CapsSerializer
    pagination_class = CapsPagination
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, )
    filter_class = CapsFilter
    authentication_classes = [JWTAuthentication, ]
    search_fields = ('name', 'description', 'category', 'size', 'manufacturer', 'price')
    ordering_fields = ('price', '-price', 'rate', 'created_at',)
    name = 'caps-list'


class CapsItemUpdateDeleteAPIview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Caps.objects.all()
    serializer_class = CapsSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, ]
    name = 'caps-detail'
    lookup_field = 'id'


class UserCapsRelationAPIview(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserCapsRelation.objects.all()
    serializer_class = UserCapsRelationSerializer
    authentication_classes = [JWTAuthentication, ]
    lookup_field = 'Caps'

    def get_object(self):
        obj, _ = UserCapsRelation.objects.get_or_create(user=self.request.user,
                                                        book_id=self.kwargs['Caps'])
        return obj


class CategoryListAPIview(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, ]

