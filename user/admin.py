from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ("email", "is_staff")
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(User, UserAdmin)
