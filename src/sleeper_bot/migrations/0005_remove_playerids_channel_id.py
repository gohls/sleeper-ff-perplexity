# Generated by Django 5.0.8 on 2024-08-25 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sleeper_bot", "0004_remove_playermetadata_rookie_year"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="playerids",
            name="channel_id",
        ),
    ]
