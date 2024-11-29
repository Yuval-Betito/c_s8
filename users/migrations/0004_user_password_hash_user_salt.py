# Generated by Django 4.2.16 on 2024-11-29 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_remove_user_password_hash_remove_user_salt"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="password_hash",
            field=models.CharField(default="", max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="salt",
            field=models.CharField(default="", max_length=50),
            preserve_default=False,
        ),
    ]