# Generated by Django 5.0.8 on 2024-10-08 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("moons", "0003_alter_evemoon_planet_alter_evemoon_reported_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="evemoon",
            name="monthly_revenue",
            field=models.IntegerField(default=0),
        ),
    ]