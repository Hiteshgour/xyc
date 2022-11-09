from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=50)