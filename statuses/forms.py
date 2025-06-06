from django import forms
from .models import Status

class StatusCreationForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('name',)

class StatusChangeForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('name',)
