# Generated by Django 4.1.7 on 2023-04-07 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0002_rename_name_profile_full_name"),
        ("workplaces", "0002_workplace_team_alter_workplace_address_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="workplace",
            name="owner",
        ),
        migrations.AddField(
            model_name="workplace",
            name="owner_profile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="profiles.profile",
                verbose_name="Perfil do usuário",
            ),
        ),
    ]
