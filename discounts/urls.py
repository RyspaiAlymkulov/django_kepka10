from django.urls import path
from discounts import views


urlpatterns = [
    path('discount/', views.MagazineDiscountListAPIview.as_view()),
    path('coupon/', views.MagazineCouponListAPIview.as_view()),
    ]