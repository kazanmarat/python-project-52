from django import forms
from .models import Status
from django.utils.translation import gettext as _

class StatusCreationForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('name',)

class StatusChangeForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('name',)
