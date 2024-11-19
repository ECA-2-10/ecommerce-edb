# Generated by Django 5.1.3 on 2024-11-19 14:30

from django.db import migrations

def add_initial_categories(apps, schema_editor):
    # Add initial product/images to the database
    Category = apps.get_model('product', 'Category')
    Category.objects.create(
        department='Cocina',
        section='Electrodomesticos'
    )

    # Sección: Utensilios de Cocina
    Category.objects.create(
        department='Cocina',
        section='Utensilios de Cocina'
    )
    
    # Sección: Pequeños Electrodomésticos
    Category.objects.create(
        department='Cocina',
        section='Pequeños Electrodomésticos'
    )

    # Sección: Almacenamiento de Alimentos
    Category.objects.create(
        department='Cocina',
        section='Almacenamiento de Alimentos'
    )

    # Sección: Otros
    Category.objects.create(
        department='Cocina',
        section='Otros'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_categories)
    ]
