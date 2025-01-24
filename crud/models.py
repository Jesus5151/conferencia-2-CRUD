from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Author(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre}"

class Book(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    precio= models.IntegerField()
