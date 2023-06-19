from django.db import models



class Clientes(models.Model):

    #verbose Name es para cuaquier tipo de campo.
    nombre=models.CharField(max_length=30,verbose_name="Nombre Cliente")
    direccion= models.CharField("Address",max_length=50)
    email=models.EmailField(blank=True,null=True)
    telefono=models.CharField(max_length=10)

    def __str__(self):

        return 'El nombre es %s la Dirección es %s y el Telefono es %s' % (self.nombre,self.direccion,self.telefono)


class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.FloatField()

    def __str__(self):
        return (self.nombre)




class Pedios(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
# Create your models here.

