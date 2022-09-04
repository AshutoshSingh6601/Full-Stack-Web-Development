from django.db import models

# Create your models here.
class Meals(models.Model):
    name=models.CharField(max_length=20)
    category=models.CharField(max_length=200)
    area=models.CharField(max_length=200)
    instructions=models.TextField(max_length=20000)
    images=models.URLField(max_length=200000)
    slug=models.SlugField(default='Ashutosh')