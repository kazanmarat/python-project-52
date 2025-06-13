from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from task_manager.custom_mixins import PlaceholderMixin

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


class CustomUserLoginForm(PlaceholderMixin, AuthenticationForm):
    pass
