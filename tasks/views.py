from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from .models import Task
from .forms import TaskCreationForm, TaskChangeForm


class CustomLoginRequiredMixin(LoginRequiredMixin):
    
    def handle_no_permission(self):
        messages.error(self.request, _('You are not logged in! Please log in.'))
        return redirect(reverse_lazy('login'))


class TaskListView(CustomLoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['id']


class TaskCreateView(CustomLoginRequiredMixin, CreateView):
    form_class = TaskCreationForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, _('Task successfully created.'))
        return response


class TaskUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskChangeForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Task successfully updated.'))
        return response


class TaskDeleteView(CustomLoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')
    template_name = 'tasks/task_delete.html'

    def test_func(self): 
        task = self.get_object()
        return task.author == self.request.user

    def handle_no_permission(self):
        if self.request.user.is_anonymous:
            return super().handle_no_permission()
        else:
            messages.error(self.request, _('Task can only be deleted by its author.'))
            return redirect(reverse_lazy('task_list'))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, _('Task successfully deleted.'))
        return response
