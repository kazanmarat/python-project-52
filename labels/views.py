from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.deletion import ProtectedError
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from .models import Label
from .forms import LabelCreationForm, LabelChangeForm


class CustomLoginRequiredMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        messages.error(self.request, _('You are not logged in! Please log in.'))
        return redirect(reverse_lazy('login'))


class LabelListView(CustomLoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'
    ordering = ['id']


class LabelCreateView(CustomLoginRequiredMixin, CreateView):
    form_class = LabelCreationForm
    success_url = reverse_lazy('label_list')
    template_name = 'labels/label_create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Label successfully created.'))
        return response


class LabelUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelChangeForm
    success_url = reverse_lazy('label_list')
    template_name = 'labels/label_update.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Label successfully updated.'))
        return response

class LabelDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Label
    context_object_name = 'label'
    success_url = reverse_lazy('label_list')
    template_name = 'labels/label_delete.html'

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, _('Label successfully deleted.'))
            return response
        except ProtectedError:
            messages.error(self.request, _('Cannot delete label because it is in use.'))
            return redirect(reverse_lazy('label_list'))
