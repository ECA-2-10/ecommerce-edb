# product/migrations/0005_auto_add_icons_to_categories.py

from django.db import migrations

def add_icons_to_categories(apps, schema_editor):
    Category = apps.get_model('product', 'Category')
    department_icons = {
        'Cocina': 'fas fa-utensils',
        'Electrónica': 'fas fa-tv',
        'Hogar': 'fas fa-couch',
        'Jardinería': 'fas fa-seedling',
        'Ropa': 'fas fa-tshirt',
        'Deportes': 'fas fa-dumbbell',
        'Belleza': 'fas fa-spa',
        'Juguetes': 'fas fa-puzzle-piece',
        'Oficina': 'fas fa-briefcase',
        'Salud': 'fas fa-heartbeat',
    }

    for department, icon in department_icons.items():
        categories = Category.objects.filter(department=department)
        categories.update(icon=icon)

class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_add_data_products'),
    ]

    operations = [
        migrations.RunPython(add_icons_to_categories),
    ]
