from django import forms

from .models import Task


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("name", "description", "status", "executor", "labels")


class TaskChangeForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("name", "description", "status", "executor", "labels")
