from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='teamImages')
    instagram = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

class Client(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='clientLogo')
    portfolio = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class Project(models.Model):
    title = models.CharField(max_length=255)
    detail = models.CharField(max_length=255)
    image1 = models.ImageField(upload_to='projectImages')
    image2 = models.ImageField(upload_to='projectImages')
    image3 = models.ImageField(upload_to='projectImages')
    image4 = models.ImageField(upload_to='projectImages')
    Url = models.CharField(max_length=255)
    date = models.DateField()
    clientName = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = RichTextField()

    




