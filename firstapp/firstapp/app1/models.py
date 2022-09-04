from email.mime import image
from django.db import models
from django.forms import IntegerField

# Create your models here.

class Product (models.Model):
    product_name=models.CharField(max_length=200)
    price=models.IntegerField()
    description=models.CharField(max_length=2000)
    stock=models.IntegerField()
    image=models.URLField(max_length=2088)

