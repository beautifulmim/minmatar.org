# Generated by Django 5.0.4 on 2024-05-05 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eveonline", "0032_evecharacter_eveonline_e_charact_d47325_idx"),
    ]

    operations = [
        migrations.AddField(
            model_name="evecharacter",
            name="exempt",
            field=models.BooleanField(default=False),
        ),
    ]
