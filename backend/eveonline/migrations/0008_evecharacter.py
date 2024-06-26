# Generated by Django 4.2.8 on 2023-12-11 20:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("eveonline", "0007_evecorporationapplication_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="EveCharacter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("character_id", models.IntegerField()),
                (
                    "character_name",
                    models.CharField(blank=True, max_length=255),
                ),
                ("corporation_id", models.IntegerField(blank=True)),
                (
                    "corporation_name",
                    models.CharField(blank=True, max_length=255),
                ),
                ("alliance_id", models.IntegerField(blank=True)),
                (
                    "alliance_name",
                    models.CharField(blank=True, max_length=255),
                ),
                ("faction_id", models.IntegerField(blank=True)),
                ("faction_name", models.CharField(blank=True, max_length=255)),
                ("skills_json", models.TextField(blank=True)),
            ],
        ),
    ]
