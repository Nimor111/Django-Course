from django.db import models
from django.utils import timezone


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)


class BlogPost(models.Model):
    title = models.CharField(unique=True, max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    content = models.TextField(default='#content')
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()

        super().save(*args, **kwargs)


class Comment(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)
    content = models.TextField(default='#content')

    post = models.ForeignKey(BlogPost, null=True, blank=True)
