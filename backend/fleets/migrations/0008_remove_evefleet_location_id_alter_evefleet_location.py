# Generated by Django 5.0.4 on 2024-05-27 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fleets", "0007_evefleetlocation"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="evefleet",
            name="location_id",
        ),
        migrations.AlterField(
            model_name="evefleet",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="fleets.evefleetlocation",
            ),
        ),
    ]