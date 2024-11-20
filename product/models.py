from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, help_text='Ingrese el nombre de un icono de Font Awesome. Ejemplo: fas fa-mobile-alt', default='fas fa-globe')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], help_text='El precio debe ser un valor positivo.')
    image = models.ImageField(upload_to='product/images', verbose_name='Imagen')
    maker = models.CharField(max_length=255)
    stock = models.IntegerField(validators=[MinValueValidator(0)], help_text='El stock debe ser igual o mayor que cero.')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name} ({self.maker})'
