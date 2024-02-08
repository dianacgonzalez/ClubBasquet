from django.db import models
from django.contrib.auth.models import User

#class Pais(models.Model):
#    nombre = models.CharField(max_length=100)

#    def __str__(self) -> str:
#        return self.nombre

#    class Meta:
#        verbose_name = "país"
#        verbose_name_plural = "países"


class Profe(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True, blank=True)
    lugar_residencia = models.CharField(max_length=100)
   # pais_origen_id = models.ForeignKey(
   #     Pais, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="País de origen"
   # )

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"
    
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacimiento = models.DateField(null=True, blank=True)
    lugar_residencia = models.CharField(max_length=100)
   # pais_origen_id = models.ForeignKey(
   #     Pais, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="País de origen"
   #)

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre} - {self.lugar_residencia}"


class Categoria(models.Model):
    nombre = models.CharField(max_length=20, verbose_name="Categoria")
    descripcion = models.CharField(max_length=100, verbose_name="Descripción", null=True)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.descripcion}"


class Equipo(models.Model):
    profe = models.ForeignKey(
        Profe, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Profesor"
        )
    categoria = models.ForeignKey(
        Categoria, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Categoria"
        )

    nombre = models.CharField(max_length=100, verbose_name="Nombre del Equipo")

    def __str__(self) -> str:
        return f"{self.profe} - {self.categoria} - {self.nombre}"

class EquipoJugador(models.Model):
    equipo = models.ForeignKey(
        Equipo, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Equipo"
        ) 
    jugador = models.ForeignKey(
        Jugador, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Jugador"
        ) 

    def __str__(self) -> str:
        return f"{self.equipo} - {self.jugador}"
