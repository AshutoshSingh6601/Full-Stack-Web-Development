from django.db import models
# Create your models here.

class Publisher(models.Model):
    name=models.CharField(max_length=100, unique=True)
    address=models.TextField(max_length=255)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=100)
    website=models.CharField(max_length=2000)

    def __str__(self):
        return self.name

class Author(models.Model):
    salutation=models.CharField(max_length=10)
    first_name=models.CharField(max_length=100, unique=True)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.first_name

class Book(models.Model):
    title=models.CharField(max_length=50)
    authors=models.ForeignKey(Author,on_delete=models.CASCADE)
    publishers=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    publication_date=models.DateField()