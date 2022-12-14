# Generated by Django 4.1.1 on 2022-10-07 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0006_profile_skill_flag"),
    ]

    operations = [
        migrations.RenameField(model_name="flag", old_name="flags", new_name="flag",),
        migrations.RenameField(
            model_name="skill", old_name="skills", new_name="skill",
        ),
        migrations.AlterField(
            model_name="profile",
            name="descripttion_app",
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name="profile",
            name="descripttion_name",
            field=models.CharField(max_length=3000),
        ),
        migrations.AlterField(
            model_name="profile",
            name="descripttion_web",
            field=models.CharField(max_length=3000),
        ),
    ]
