# Generated by Django 5.1.2 on 2025-05-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eveonline", "0048_evecharacter_user_eveprimarycharacter_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evecharacterkillmailattacker",
            name="character_id",
            field=models.BigIntegerField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name="evecharacterkillmailattacker",
            name="ship_type_id",
            field=models.BigIntegerField(db_index=True, null=True),
        ),
    ]
