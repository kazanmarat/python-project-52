from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    name = models.CharField(_("name"), max_length=50, unique=True)
    date_creation = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = _("Status")
        verbose_name_plural = _("Statuses")

    def __str__(self):
        return self.name
