from django.db import models

# Create your models here.
class Student(models.Model):
    registration_no = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)

    def __str__(self):
        return self.registration_no