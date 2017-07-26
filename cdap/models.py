from django.db import models


# Create your models here.
class Locacion(models.Model):
    nombre= models.CharField(max_length=50)
    comentario= models.TextField()
    activo= models.BooleanField()

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre= models.CharField(max_length=50)
    direccion= models.TextField()
    telefono= models.CharField(max_length=12)
    responsable= models.CharField(max_length=120)
    email= models.EmailField()
    fecha_alta= models.DateTimeField(auto_now_add=True) # Esto es para que se agregue sola y no se modifique
    fecha_ultima_mod= models.DateField(auto_now=True) # Esto es para que se agregue sola
    comentario= models.TextField()
    activo= models.BooleanField()
    locacion= models.ManyToManyField(Locacion)

    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=70)
    documento= models.CharField(max_length=10)
    foto= models.ImageField(upload_to="personas/archivo/%Y/%m/%d", null=True, blank=True)
    fecha_alta= models.DateField(auto_now_add=True)
    fecha_ultima_mod= models.DateField(auto_now=True)
    activo= models.BooleanField()
    empresa= models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + ' ' + self.apellido
