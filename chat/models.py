from django.db import models
#from django.contrib.auth.models import  User
# Create your models here.
from user.models import User


class Group(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="members")

    class Meta:
        db_table = "group"




