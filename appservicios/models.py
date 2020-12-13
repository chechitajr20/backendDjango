from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.usuario

class Cliente(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=25)
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ('nombre',)
    
class Servicios(models.Model):
    servicio = models.CharField(max_length=25)
    descripcion = models.TextField()

    def __str__(self):
        return self.servicio

    class Meta:
        ordering = ('servicio',)

class Contratos(models.Model):
    fecha = models.DateField()
    costo = models.IntegerField()
    clientes = models.ManyToManyField(Cliente)
    servicios = models.ManyToManyField(Servicios)

    def __str__(self):
        return self.fecha
    
    class Meta:
        ordering = ('fecha',)
 