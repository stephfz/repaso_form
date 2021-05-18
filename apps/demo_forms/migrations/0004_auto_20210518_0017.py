# Generated by Django 2.2.4 on 2021-05-18 00:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_forms', '0003_auto_20210517_2128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hobbie',
            name='name',
        ),
        migrations.AlterField(
            model_name='hobbie',
            name='tipo',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)]),
        ),
    ]
