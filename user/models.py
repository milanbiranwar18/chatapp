from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    mob_number = models.IntegerField(default=10)
    location = models.CharField(max_length=200)