import moneyed
from djmoney.models.fields import MoneyField

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Offer(models.Model):
    title = models.CharField(max_length=200)
    price = MoneyField(default=100, max_digits=10, decimal_places=2, default_currency='EUR')
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='pics/', null=True, blank=True)

    category = models.ForeignKey(Category, null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True)
