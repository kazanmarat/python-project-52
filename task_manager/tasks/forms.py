from django import forms

from .models import Task


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ["author", "date_creation"]


class TaskChangeForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ["author", "date_creation"]
