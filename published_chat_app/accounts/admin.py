from django.contrib import admin
from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)

# @admin.site.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display=('Name','email',)

# Register your models here.
