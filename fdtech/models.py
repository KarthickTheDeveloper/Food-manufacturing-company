from django.db import models

# Create your models here.
class Techmodel(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=20)