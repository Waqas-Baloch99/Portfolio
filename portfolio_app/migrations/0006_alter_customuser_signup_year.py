# Generated by Django 5.1.3 on 2024-12-04 10:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0005_payment_payment_method_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='signup_year',
            field=models.PositiveIntegerField(default=2024, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2024)]),
        ),
    ]
