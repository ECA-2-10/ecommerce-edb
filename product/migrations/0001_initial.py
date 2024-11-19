# Generated by Django 5.1.3 on 2024-11-17 13:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=125)),
                ('description', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, help_text='El precio debe ser un valor positivo.', max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('image', models.ImageField(upload_to='products', verbose_name='Imagen')),
                ('maker', models.CharField(max_length=255)),
                ('stock', models.IntegerField(help_text='El stock debe ser igual o mayor que cero.', validators=[django.core.validators.MinValueValidator(0)])),
                ('department', models.CharField(max_length=255)),
                ('section', models.CharField(max_length=255)),
            ],
        ),
    ]