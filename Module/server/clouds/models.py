from django.db import models

# Create your models here.
class Clog(models.Model):
    CID = models.IntegerField(max_length=50)
    CU = models.CharField(max_length=50)
    MU = models.CharField(max_length=50)
    DI = models.CharField(max_length=50)
    DO = models.CharField(max_length=50)
    NI = models.CharField(max_length=50)
    NO = models.CharField(max_length=50)
    UPT = models.CharField(max_length=50)
    TSP = models.DateTimeField(auto_now = True)