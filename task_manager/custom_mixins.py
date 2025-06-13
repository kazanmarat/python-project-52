from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class CustomLoginRequiredMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        messages.error(self.request, _("You are not logged in! Please log in."))
        return redirect(reverse_lazy("login"))


class CustomUserPassesTestMixin(UserPassesTestMixin):
    def test_func(self):
        profile = self.get_object()
        return profile == self.request.user

    def handle_no_permission(self):
        if self.request.user.is_anonymous:
            messages.error(
                self.request, _("You are not logged in! Please log in.")
            )
            return redirect(reverse_lazy("login"))
        else:
            messages.error(
                self.request,
                _("You do not have permission to modify another user."),
            )
            return redirect(reverse_lazy("user_list"))


class PlaceholderMixin:
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})


