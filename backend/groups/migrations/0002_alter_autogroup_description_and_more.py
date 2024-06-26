# Generated by Django 4.2.10 on 2024-02-15 12:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("groups", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autogroup",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="autogroup",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="requestablegroup",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="requestablegroup",
            name="image_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="requestablegroup",
            name="required_groups",
            field=models.ManyToManyField(
                blank=True, related_name="required_by", to="auth.group"
            ),
        ),
    ]
