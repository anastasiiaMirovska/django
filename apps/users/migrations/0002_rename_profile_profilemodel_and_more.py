# Generated by Django 5.1 on 2024-08-12 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='ProfileModel',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
