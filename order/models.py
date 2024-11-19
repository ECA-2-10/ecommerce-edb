from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError  
from django.utils.timezone import now 

def validate_delivery_date(value):
    if value < now():
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
    deliveryDate = models.DateTimeField(validators=[validate_delivery_date])

    def __str__(self):
        return f'Pedido {self.id} - {self.email}'
