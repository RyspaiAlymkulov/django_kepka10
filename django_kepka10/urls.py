from django.contrib import admin
from django.urls import path, include
from . import swagger
from custom_caps import views
from rest_framework import routers

ROUTER = routers.DefaultRouter()
ROUTER.register(r'caps', views.CapsListAPIview, basename='caps')

urlpatterns = [
    path('admin/', admin.site.urls),


    path(r'^', include(ROUTER.urls), name="custom_caps"),


    path('api/v1/magazine/', views.MagazineListAPIview.as_view()),
    path('api/v1/magazine/<int:id>/', views.MagazineItemUpdateDeleteAPIview.as_view()),
    path('api/v1/manufacturer/', views.ManufacturerListAPIview.as_view()),
    path('api/v1/manufacturer/<int:id>/', views.ManufacturerItemUpdateDeleteAPIview.as_view()),
    path('api/v1/caps/<int:id>/', views.CapsItemUpdateDeleteAPIview.as_view()),
    path('api/v1/category/', views.CategoryListAPIview.as_view()),


    path('api/v1/user/', include('user.urls')),
    path('api/v1/cart/', include('cart.urls')),
    path('api/v1/discounts/', include('discounts.urls')),
    path('api/v1/socialMedia/', include('social_media.urls'))
]

urlpatterns += swagger.urlpatterns
