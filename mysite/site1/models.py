from email.mime import image
from django.db import models

# Create your models here.

class Product (models.Model):
    product_name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField(max_length=2000)
    stock=models.IntegerField()
    image=models.URLField(max_length=2088)
