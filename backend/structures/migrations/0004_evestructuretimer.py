# Generated by Django 5.0.6 on 2024-06-23 02:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("structures", "0003_alter_evestructure_fuel_expires_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EveStructureTimer",
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
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("anchoring", "Anchoring"),
                            ("armor", "Armor"),
                            ("hull", "Hull"),
                            ("unanchoring", "Unanchoring"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("astrahus", "Astrahus"),
                            ("fortizar", "Fortizar"),
                            ("keepstar", "Keepstar"),
                            ("raitaru", "Raitaru"),
                            ("azbel", "Azbel"),
                            ("sotiyo", "Sotiyo"),
                            ("athanor", "Athanor"),
                            ("tatara", "Tatara"),
                            ("tenebrex_cyno_jammer", "Tenebrex Cyno Jammer"),
                            ("pharolux_cyno_beacon", "Pharolux Cyno Beacon"),
                            ("ansiblex_jump_gate", "Ansiblex Jump Gate"),
                        ],
                        max_length=255,
                    ),
                ),
                ("timer", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("system_name", models.CharField(max_length=255)),
                (
                    "corporation_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "alliance_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="structures_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "structure",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="structures.evestructure",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="structures_updated_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]