from django.db import models

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=231)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    favourite_anime = models.CharField(max_length=100)