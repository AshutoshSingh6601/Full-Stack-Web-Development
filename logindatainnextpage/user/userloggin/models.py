
from django.db import models


# Create your models here.
class Loggin(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=50)
    date_time=models.DateTimeField()