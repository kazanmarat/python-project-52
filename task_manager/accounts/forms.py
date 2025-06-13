from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username")


class CustomUserUpdateForm(CustomUserCreationForm):
    def clean_username(self):
        current_username = self.instance.username
        new_username = self.cleaned_data.get("username")
        if current_username == new_username:
            return new_username
        return super().clean_username()

class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})

class CustomUserLoginForm(PlaceholderMixin, AuthenticationForm):
    pass
