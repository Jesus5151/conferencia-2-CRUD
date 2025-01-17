from django.db import models

# Create your models here.

from django.contrib.auth.models import User



class Book(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    precio= models.IntegerField()
