from django.db import models


class Song(models.Model):
    link = models.URLField()
    email = models.EmailField()
