from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from statuses.models import Status
from accounts.models import CustomUser


class Task(models.Model):
    name = models.CharField(_("name"), max_length=150, unique=True)
    description = models.TextField(_("description"), null=True, blank=True)
    status = models.ForeignKey(Status, verbose_name=_("Status"), on_delete=models.PROTECT)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        related_name='author'
        )
    executor = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        null=True, blank=True,
        related_name='executor',
        verbose_name=_('Executor'),
        )
    tag = models.CharField(_("Tags"), max_length=150, null=True, blank=True)
    date_creation = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
    
    def __str__(self):
        return self.name

