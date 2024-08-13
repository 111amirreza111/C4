from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=500)
    password = models.CharField(max_length=500)