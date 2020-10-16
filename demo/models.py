from django.db import models
from django.contrib.auth.models import  auth, User


# Create your models here.

class Details(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Street = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Pincode = models.IntegerField()
    Age = models.IntegerField()


