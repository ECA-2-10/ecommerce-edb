# Generated by Django 5.1.3 on 2024-11-20 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_category_department_remove_product_producttype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(default='fas fa-globe', help_text='Ingrese el nombre de un icono de Font Awesome. Ejemplo: fas fa-mobile-alt', max_length=50),
        ),
    ]
