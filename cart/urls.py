from django.urls import path
from cart import views


urlpatterns = [
    path('cart/', views.CartListAPIview.as_view()),
    path('register/', views.UserListAPIview.as_view()),
    path('userprofile/', views.DeliveryListAPIview.as_view()),
]