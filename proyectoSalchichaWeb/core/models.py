from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.

class Cliente(models.Model):
    rut_cliente = models.CharField(max_length=100)
    nombre_cliente = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return str(self.rut_cliente)


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='producto')

    def __str__(self):
        return str(self.nombre)


class Boleta(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    METODO_PAGO_CHOICES = [
        ('efectivo', 'Efectivo (pago en local)'),
        ('debito', 'Tarjeta de débito'),
        ('credito', 'Tarjeta de crédito'),
    ]
    metodo_pago = models.CharField(max_length=30, choices=METODO_PAGO_CHOICES)
    total = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)


class DetalleBoleta(models.Model):
    producto = models.ForeignKey('Producto', on_delete=CASCADE)
    boleta = models.ForeignKey('Boleta', on_delete=CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.PositiveIntegerField()

    def __str__(self):
        return str(self.boleta)
