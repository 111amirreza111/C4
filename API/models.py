from django.db import models


# Create your models here.
class PrototypeToken(models.Model):
    token = models.CharField(max_length=1000)

# Create your models here.
class PrototypeRequestDB(models.Model):
    token = models.CharField(max_length=1000)   
    req = models.CharField(max_length=1000)
    reqID = models.IntegerField()
    status = models.CharField(max_length=1000)

  