from django.contrib import admin
from custom_caps.models import Magazine, Manufacturer, Caps, UserCapsRelation, Category


admin.site.register(Magazine),
admin.site.register(Manufacturer)
admin.site.register(Caps)
admin.site.register(UserCapsRelation)
admin.site.register(Category)
