from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.email

class Artist(models.Model):
    name = models.CharField(max_length=120)
    nationality = models.CharField(max_length=255, blank=True)
    residence = models.TextField(blank=True)
    yearofbirth = models.TextField(blank=True)
    yearofdeath = models.TextField(blank=True)
    styles = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

class Artwork(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120, blank=True)
    year = models.CharField(max_length=120, blank=True)
    medium = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=120, blank=True)
    notes = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title
    
