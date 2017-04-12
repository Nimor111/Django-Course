import moneyed
from djmoney.models.fields import MoneyField

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from .query import OfferQuerySet


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Offer(models.Model):
    PENDING = 'p'
    APPROVED = 'a'
    REJECTED = 'r'
    STATUS_CHOICES = (
        (PENDING, 'pending'),
        (APPROVED, 'approved'),
        (REJECTED, 'rejected'),
    )
    title = models.CharField(max_length=200, default="Title")
    price = MoneyField(default=100, max_digits=10, decimal_places=2, default_currency='EUR')
    description = models.TextField(default="Description")
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='pics/', null=True, blank=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=PENDING,
    )

    category = models.ForeignKey(Category, null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True)

    objects = OfferQuerySet.as_manager()
