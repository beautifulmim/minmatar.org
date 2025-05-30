# Generated by Django 5.1.2 on 2025-05-26 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eveonline", "0060_evelocation"),
        ("structures", "0011_evestructuremanager"),
    ]

    operations = [
        migrations.AddField(
            model_name="evestructuremanager",
            name="last_polled",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="evestructuremanager",
            name="character",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="eveonline.evecharacter",
            ),
        ),
        migrations.AlterField(
            model_name="evestructuremanager",
            name="last_update",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="evestructuremanager",
            name="poll_time",
            field=models.IntegerField(default=0),
        ),
    ]
