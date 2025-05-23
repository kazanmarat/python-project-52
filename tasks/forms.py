from django import forms
from .models import Task


class TaskCreationForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor', 'tag',)


class TaskChangeForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor', 'tag',)
