from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserUpdateForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserUpdateForm
    model = CustomUser
    list_display = [
        "first_name",
        "last_name",
        "username",
        "is_staff",
        "is_active",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
