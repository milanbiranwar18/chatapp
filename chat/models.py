from django.db import models

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)

    class Meta:
        db_table = "group"