from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Category(models.Model):
    department = models.CharField(max_length=255)
    section = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='fas fa-utensils')

    def __str__(self):
        return f'{self.department}, {self.section}'

class Product(models.Model):
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], help_text='El precio debe ser un valor positivo.')
    image = models.ImageField(upload_to='product/images', verbose_name='Imagen')
    maker = models.CharField(max_length=255)
    stock = models.IntegerField(validators=[MinValueValidator(0)], help_text='El stock debe ser igual o mayor que cero.')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f'{self.name} ({self.maker})'
