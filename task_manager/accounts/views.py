from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.custom_mixins import CustomUserPassesTestMixin

from .forms import (
    CustomUserCreationForm,
    CustomUserLoginForm,
    CustomUserUpdateForm,
)
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "account/user_signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _("User registered successfully"))
        return response


class UserLoginView(LoginView):
    template_name = "account/user_login.html"
    form_class = CustomUserLoginForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _("You are logged in."))
        return response


class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(self.request, _("You are logged out."))
        return super().dispatch(request, *args, **kwargs)


class UserListView(ListView):
    model = CustomUser
    template_name = "account/user_list.html"
    context_object_name = "users"
    ordering = ["id"]


class UserUpdateView(CustomUserPassesTestMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = "account/user_update.html"
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _("User successfully updated."))
        return response


class UserDeleteView(CustomUserPassesTestMixin, DeleteView):
    model = CustomUser
    context_object_name = "user"
    template_name = "account/user_delete.html"
    success_url = reverse_lazy("user_list")

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, _("User successfully deleted."))
            return response
        except ProtectedError:
            messages.error(
                self.request, _("Cannot delete user because it is in use.")
            )
            return redirect(reverse_lazy("user_list"))
