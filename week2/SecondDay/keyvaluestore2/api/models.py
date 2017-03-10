from django.db import models
from django.utils import timezone
import uuid


# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)

    def to_s(self):
        return str(self.id)


class Data(models.Model):
    key = models.CharField(max_length=300)
    value = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, null=True, blank=True)
