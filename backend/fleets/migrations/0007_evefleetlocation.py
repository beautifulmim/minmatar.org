# Generated by Django 5.0.4 on 2024-05-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "fleets",
            "0006_evestandingfleet_evestandingfleetcommanderlog_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="EveFleetLocation",
            fields=[
                (
                    "location_id",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("location_name", models.CharField(max_length=255)),
            ],
        ),
    ]