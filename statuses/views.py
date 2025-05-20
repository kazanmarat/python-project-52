from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from .models import Status
from .forms import StatusCreationForm, StatusChangeForm


class CustomLoginRequiredMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        messages.error(self.request, _('You are not logged in! Please log in.'))
        return redirect(reverse_lazy('login'))


class StatusListView(CustomLoginRequiredMixin, ListView):
    model = Status
    template = 'statuses/status_list.html'
    context_object_name = 'statuses'
    ordering = ['id']


class StatusCreateView(CustomLoginRequiredMixin, CreateView):
    form_class = StatusCreationForm
    success_url = reverse_lazy('status_list')
    template_name = 'statuses/status_create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Status successfully created.'))
        return response


class StatusUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusChangeForm
    success_url = reverse_lazy('status_list')
    template_name = 'statuses/status_update.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Status successfully updated.')) # Статус успешно изменен.
        return response

class StatusDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Status
    context_object_name = 'status'
    success_url = reverse_lazy('status_list')
    template_name = 'statuses/status_delete.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Status successfully deleted.')) # Статус успешно удален.
        return response
