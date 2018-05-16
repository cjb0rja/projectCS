from django.db import models
from django.conf import settings


# Create your models here.

class Vaccine(models.Model):
    vaccine_name = models.CharField(max_length=200)
    date= models.DateField(auto_now=False, auto_now_add=False)
