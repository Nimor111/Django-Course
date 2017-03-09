from django.db import models
import uuid


class Data(models.Model):
    key = models.CharField(max_length=300)
    value = models.CharField(max_length=300)


# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.ForeignKey(Data, null=True, blank=True)
