# Generated by Django 5.1.1 on 2024-09-13 15:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("moons", "0002_remove_evemoon_owned_by_ticker"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="evemoon",
            name="planet",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="evemoon",
            name="reported_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]