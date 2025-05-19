from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.utils.translation import gettext as _
from .models import CustomUser
from .forms import CustomUserCreationForm
    

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/user_signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('You are registered.'))
        return response


class UserLoginView(LoginView):
    template_name = 'account/user_login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('You are logged in.'))
        return response


class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(self.request, _('You are logged out.'))
        return super().dispatch(request, *args, **kwargs)


class UserListView(ListView):
    model = CustomUser
    template_name = 'account/user_list.html'
    context_object_name = 'users'
    ordering = ['id']


class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = CustomUser
    template_name = 'account/user_update.html'
    fields = ('first_name', 'last_name','username', 'password')
    success_url = reverse_lazy('user_list')
    
    def test_func(self): 
        profile = self.get_object() 
        return profile.id == self.request.user.id

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('User successfully updated.'))
        return response
    
    def handle_no_permission(self):
        if self.request.user.is_anonymous:
            messages.error(self.request, _('You are not logged in! Please log in.'))
            return redirect(reverse_lazy('login'))
        else:
            messages.error(self.request, _('You do not have permission to modify another user.'))
            return redirect(reverse_lazy('user_list'))


class UserDeleteView(UserPassesTestMixin, DeleteView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'account/user_delete.html'
    success_url = reverse_lazy('user_list')

    def test_func(self): 
        profile = self.get_object() 
        return profile.id == self.request.user.id

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('User successfully deleted.'))
        return response

    def handle_no_permission(self):
        if self.request.user.is_anonymous:
            messages.error(self.request, _('You are not logged in! Please log in.'))
            return redirect(reverse_lazy('login'))
        else:
            messages.error(self.request, _('You do not have permission to modify another user.'))
            return redirect(reverse_lazy('user_list'))

