# Generated by Django 5.0.4 on 2024-04-11 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0007_alter_sigrequest_sig_alter_teamrequest_team"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="requestablegroup",
            name="group",
        ),
        migrations.RemoveField(
            model_name="requestablegroup",
            name="group_managers",
        ),
        migrations.RemoveField(
            model_name="requestablegroup",
            name="required_groups",
        ),
        migrations.DeleteModel(
            name="GroupRequest",
        ),
        migrations.DeleteModel(
            name="RequestableGroup",
        ),
    ]
