from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=30)
    sigla = models.CharField(max_length=10)

    def __str__(self):
        return self.sigla


class Estudiante(models.Model):
    ci = models.CharField(primary_key=True, max_length=20, null=False)
    nombres = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    matricula = models.PositiveIntegerField()
    carrera = models.ManyToManyField(Carrera)
    fecha_de_nacimento = models.DateField()
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.ci
