from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, auto_created=True)
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], help_text='El precio debe ser un valor positivo.')
    image = models.ImageField(upload_to='products', verbose_name='Imagen')
    maker = models.CharField(max_length=255)
    stock = models.IntegerField(validators=[MinValueValidator(0)], help_text='El stock debe ser igual o mayor que cero.')
    department = models.CharField(max_length=255)
    section = models.CharField(max_length=255)

    # Comprobar que va bien este formato para mostrar el nombre
    def __str__(self):
        return f'Producto: {self.nombre}'