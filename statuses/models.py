from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Status(models.Model):
    # name = models.CharField(max_length=50)
    name = models.CharField(_("name"), max_length=50, unique=True)
    date_creation = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
