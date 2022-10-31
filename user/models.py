from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mob_number = models.IntegerField(default=10)
    location = models.CharField(max_length=200)