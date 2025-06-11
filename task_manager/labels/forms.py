from django import forms

from .models import Label


class LabelCreationForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ("name",)


class LabelChangeForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ("name",)
