from django.db import models
import uuid

from users.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True, max_length=255)


class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(unique=True, max_length=255)

    comments = models.ManyToManyField(User, through='comments.Comment')
    categories = models.ManyToManyField(Category, related_name='products')
