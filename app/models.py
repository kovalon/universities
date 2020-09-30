from django.db import models


# Create your models here.
class University(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    subjects = models.TextField()
