# Generated by Django 5.0.8 on 2024-08-20 10:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_usermodel_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(150)]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='name',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[A-Z][a-zA-Z]{1,19}$', 'First letter uppercase, min 2, max 20')]),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='surname',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[A-Z][a-zA-Z]{1,19}$', 'First letter uppercase, min 2, max 20')]),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='password',
            field=models.CharField(max_length=128, validators=[django.core.validators.RegexValidator('^(?=.*\\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\\w\\d\\s:])(\\S){8,18}$', ['Password must contain at least 1 number (1-9)', 'Password must contain at least 1 uppercase letter', 'Password must contain at least 1 lowercase letter', 'Password must contain at least 1 special character', 'Password must contain min 8 max 16 characters without spaces'])], verbose_name='password'),
        ),
    ]
