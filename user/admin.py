from django.contrib import admin

from user.models import CustomUserManager, CustomUser

admin.site.register(CustomUser)