from django.urls import path
from user.views import RequestPasswordResetEmail, PasswordTokenCheckAPI, SetNewPasswordAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from user import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('tokenrefresh/', TokenRefreshView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete'),
    path('profile/', views.ProfileUser.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),
]

