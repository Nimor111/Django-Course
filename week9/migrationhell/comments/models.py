from django.db import models
from users.models import User
from products.models import Product


# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments')
    product = models.ForeignKey(Product)
    text = models.TextField()
