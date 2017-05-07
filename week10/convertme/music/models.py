from django.db import models


# Create your models here.
class Song(models.Model):
    link = models.URLField()
    email = models.EmailField()
