# Generated by Django 5.2 on 2025-05-21 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0002_alter_status_date_creation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Statuses'},
        ),
        migrations.AlterField(
            model_name='status',
            name='date_creation',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='name'),
        ),
    ]
