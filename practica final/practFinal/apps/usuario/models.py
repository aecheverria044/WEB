from django.db import models

#create your models here
class usuario(models.Model):
    nombre = models.CharField(max_length=50) #con esto entra el required
    pais = models.TextField(max_length=50)
    ciudad = models.TextField(max_length=50)
    domicilio = models.TextField(max_length=300)
    sexo =models.TextField(max_length=1)
    edad = models.IntegerField(max_length=3)
    areamedica =models.TextField(blank=True, null=True)
    repEnfermedad =models.TextField(blank=True, null=True)
    duracion =models.TextField(blank=True, null=True)
    comentarios =models.TextField(blank=True, null=True)
    contraseña =models.TextField()
