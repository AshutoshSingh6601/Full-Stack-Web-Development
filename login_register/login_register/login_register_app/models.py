from tkinter import CASCADE
from django.db import models

# Create your models here.


class Register(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    address=models.TextField(max_length=1000)

class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.ForeignKey(Register,on_delete=models.CASCADE)
    # registers=models.ForeignKey(Register,on_delete=models.CASCADE)