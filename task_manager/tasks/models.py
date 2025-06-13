from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from task_manager.accounts.models import CustomUser
from task_manager.labels.models import Label
from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(_("name"), max_length=150, unique=True)
    description = models.TextField(_("description"), null=True, blank=True)
    status = models.ForeignKey(
        Status, verbose_name=_("Status"), on_delete=models.PROTECT
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        related_name="author",
    )
    executor = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="executor",
        verbose_name=_("Executor"),
    )
    labels = models.ManyToManyField(
        Label,
        verbose_name=_("Label"),
        blank=True,
        through="TaskLabel",
        through_fields=("task", "label"),
    )
    date_creation = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return self.name


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)
