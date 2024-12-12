from django.db import models

class Municipio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre