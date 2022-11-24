from django.db import models

# Create your models here.
class torneo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class Equipos(models.Model):
    nombre=models.CharField(max_length=50)
    abreviatura=models.CharField(max_length=20)
    aniofundacion=models.IntegerField()


class Jugadores(models.Model):
    num_pasaporte=models.IntegerField()
    nombre=models.CharField(max_length=50)
    nacionalidad=models.CharField(max_length=20)
    edad=models.IntegerField()
    posicion=models.CharField(max_length=50, blank=True)
    abr_posicion=models.CharField(max_length=20, blank=True)
    num_dorsal=models.IntegerField(blank=True, null=True, default=0)
    cargo=models.CharField(max_length=50, blank=True)
    abr_cargo=models.CharField(max_length=20, blank=True)
    equipo_id=models.IntegerField() 


class Staff(models.Model):
    num_pasaporte=models.IntegerField()
    nombre=models.CharField(max_length=50)
    nacionalidad=models.CharField(max_length=20)
    edad=models.IntegerField()
    cargo=models.CharField(max_length=50, blank=True)
    abr_cargo=models.CharField(max_length=20)
    equipo_id=models.IntegerField() 

