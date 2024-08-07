# Generated by Django 5.0.4 on 2024-05-22 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fleets", "0002_evefleetnotificationchannel_group_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="evefleet",
            name="location_id",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="evefleet",
            name="type",
            field=models.CharField(
                choices=[
                    ("stratop", "Strategic Operation"),
                    ("non_strategic", "Non Strategic Operation"),
                    ("training", "Training Operation"),
                ],
                max_length=32,
            ),
        ),
    ]
