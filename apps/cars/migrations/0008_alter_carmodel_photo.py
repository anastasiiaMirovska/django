# Generated by Django 5.1 on 2024-08-14 12:03

from django.db import migrations, models

import core.services.file_service


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_carmodel_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='photo',
            field=models.ImageField(blank=True, upload_to=core.services.file_service.FileService.upload_car_photo),
        ),
    ]
