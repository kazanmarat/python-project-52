from django.contrib import admin

from .forms import TaskChangeForm, TaskCreationForm
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    add_form = TaskCreationForm
    form = TaskChangeForm
    model = Task
    fields = ("name", "description", "status", "author", "executor", "tag")


admin.site.register(Task, TaskAdmin)
