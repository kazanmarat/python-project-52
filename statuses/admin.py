from django.contrib import admin

# Register your models here.
from .forms import StatusChangeForm, StatusCreationForm
from .models import Status


class StatusAdmin(admin.ModelAdmin):
    fields = ['name', 'date_creation']
    # add_form = StatusCreationForm
    # form = StatusChangeForm
    # model = Status
    # list_display = [
    #     'name',
    #     'date_creation',
    # ]


admin.site.register(Status)