# Generated by Django 5.0.4 on 2024-04-12 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eveonline", "0029_alter_evecharacter_token"),
        (
            "eveuniverse",
            "0010_alter_eveindustryactivityduration_eve_type_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="evecharacter",
            name="alliance",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="eveonline.evealliance",
            ),
        ),
        migrations.AddField(
            model_name="evecharacter",
            name="faction",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="eveuniverse.evefaction",
            ),
        ),
    ]
