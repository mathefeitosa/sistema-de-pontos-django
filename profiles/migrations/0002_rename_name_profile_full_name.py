# Generated by Django 4.1.7 on 2023-04-07 16:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="name",
            new_name="full_name",
        ),
    ]
