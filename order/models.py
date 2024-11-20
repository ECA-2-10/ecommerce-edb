from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError  
from django.utils.timezone import now 
from account.models import CustomUser
from product.models import Product

def validate_delivery_date(value):
    if value < now().date():
        raise ValidationError("The delivery date cannot be in the past.")

# Create your models here.
class Order(models.Model):
    email = models.EmailField(max_length=125)
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
        help_text='El total debe ser un valor positivo.'
    )
    address = models.CharField(max_length=255)
    delivered = models.BooleanField(default=False)
    ON_DELIVERY = "OD"
    CREDIT_CARD = "CC"
    PAYMENT_METHODS = [
        (ON_DELIVERY, "On Delivery"),
        (CREDIT_CARD, "Credit Card"),
    ]
    paymentMethod = models.CharField(
        max_length=2,
        choices=PAYMENT_METHODS,
        default=ON_DELIVERY
    )
    deliveryDate = models.DateField(validators=[validate_delivery_date])
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)

    def __str__(self):
        return f'Pedido {self.id} - {self.email}'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_products')
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        help_text='La cantidad debe ser al menos 1.'
    )

    def __str__(self):
        return f'{self.quantity} x {self.product.name} en {self.order}'