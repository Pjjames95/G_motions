from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "is_active", "is_staff", "date_joined", "last_login")
    list_filter = ("is_active", "is_staff", "date_joined")
    search_fields = ("username", "email")
    ordering = ("username",)