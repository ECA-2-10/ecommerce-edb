# product/migrations/0005_auto_add_icons_to_categories.py

from django.db import migrations

def add_icons_to_departments(apps, schema_editor):
    Department = apps.get_model('product', 'Department')
    department_icons = {
        'Cocina': 'fas fa-utensils',
        'Electrónica': 'fas fa-tv',
        'Hogar': 'fas fa-couch',
        'Jardinería': 'fas fa-seedling',
        'Deportes': 'fas fa-dumbbell',
        'Oficina': 'fas fa-briefcase',
        'Salud': 'fas fa-heartbeat',
    }

    for name_department, icon in department_icons.items():
        department = Department.objects.filter(name=name_department)
        department.update(icon=icon)

class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_add_data_products'),
    ]

    operations = [
        migrations.RunPython(add_icons_to_departments),
    ]
