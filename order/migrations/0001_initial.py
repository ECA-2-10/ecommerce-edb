# Generated by Django 5.1.3 on 2024-11-20 11:33

import django.core.validators
import django.db.models.deletion
import order.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0004_auto_update_icons_categories'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=125)),
                ('total', models.DecimalField(decimal_places=2, help_text='El total debe ser un valor positivo.', max_digits=10, validators=[django.core.validators.MinValueValidator(0.01)])),
                ('address', models.CharField(max_length=255)),
                ('delivered', models.BooleanField(default=False)),
                ('paymentMethod', models.CharField(choices=[('OD', 'On Delivery'), ('CC', 'Credit Card')], default='OD', max_length=2)),
                ('deliveryDate', models.DateField(validators=[order.models.validate_delivery_date])),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, help_text='La cantidad debe ser al menos 1.', validators=[django.core.validators.MinValueValidator(1)])),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='product.product')),
            ],
        ),
    ]
