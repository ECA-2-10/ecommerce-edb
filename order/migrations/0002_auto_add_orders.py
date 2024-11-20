# Generated by Django 5.1.3 on 2024-11-20 13:40

from django.db import migrations
from datetime import timedelta
from django.utils.timezone import now
import random
import string

def add_initial_orders(apps, schema_editor):

    Order = apps.get_model('order', 'Order')
    OrderProduct = apps.get_model('order', 'OrderProduct')
    Product = apps.get_model('product', 'Product')

    initial_orders = [
        ({   
            "code": "F9ZNWNUQFR",
            "email": "client1@example.com",
            "total": 5899.97,
            "address": "123 Main Street",
            "paymentMethod": "CC",
            "deliveryDate": now().date() + timedelta(days=5),
        },[(1,2),(2,1)]),
        ({
            "code": "DD1FYYBF76",
            "email": "client1@example.com",
            "total": 1799.96,
            "address": "456 Elm Street",
            "paymentMethod": "OD",
            "deliveryDate": now().date() + timedelta(days=3),
        },[(3,1),(4,3)]),
        ({
            "code": "A7XT1VMD6Y",
            "email": "client2@example.com",
            "total": 399.99,
            "address": "789 Oak Avenue",
            "paymentMethod": "CC",
            "deliveryDate": now().date() + timedelta(days=7),
        },[(5,1)]),
        ({
            "code": "B3LN5H2Z0P",
            "email": "client2@example.com",
            "total": 599.97,
            "address": "101 Pine Road",
            "paymentMethod": "OD",
            "deliveryDate": now().date() + timedelta(days=10),
        },[(6,2),(3,1)]),
        ({
            "code": "T9V8Q2W6R1",
            "email": "client3@example.com",
            "total": 5199.94,
            "address": "202 Maple Street",
            "paymentMethod": "CC",
            "deliveryDate": now().date() + timedelta(days=2),
        },[(1,1),(2,2),(3,3)]),
        ({
            "code": "R2T7F9B4VQ",
            "email": "client3@example.com",
            "total": 3129.94,
            "address": "303 Birch Avenue",
            "paymentMethod": "OD",
            "deliveryDate": now().date() + timedelta(days=4),
        },[(7,1),(8,5)]),
        ({
            "code": "D5Q3X2Y9P0",
            "email": "client4@example.com",
            "total": 429.97,
            "address": "404 Cedar Street",
            "paymentMethod": "CC",
            "deliveryDate": now().date() + timedelta(days=6),
        },[(9,1),(10,1),(11,1)]),
        ({
            "code": "M4P1B9Q8J6",
            "email": "client4@example.com",
            "total": 1999.94,
            "address": "505 Oak Drive",
            "paymentMethod": "OD",
            "deliveryDate": now().date() + timedelta(days=8),
        },[(12,1),(13,2),(14,3)]),
        ({
            "code": "F2V0D9W5JQ",
            "email": "client5@example.com",
            "total": 2739.93,
            "address": "606 Elm Drive",
            "paymentMethod": "CC",
            "deliveryDate": now().date() + timedelta(days=1),
        },[(15,2),(16,1),(17,1),(18,1),(19,2)]),
        ({
            "code": "B7N5Q3T1FD",
            "email": "client5@example.com",
            "total": 169.98,
            "address": "707 Pine Lane",
            "paymentMethod": "OD",
            "deliveryDate": now().date(),
            "delivered": True
        },[(20,1),(28,1)])
    ]

    for (order_data, product_orders) in initial_orders:
        order = Order.objects.create(**order_data)

        for (product_id, quantity) in product_orders:
            order_product = OrderProduct.objects.create(
                order=order,
                product = Product.objects.get(id=product_id),
                quantity=quantity
            )
   

class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_initial_orders),
    ]