import json
import uuid
import glob

from store.models import User, Data
from django.conf import settings


def create_user():
    identifier = str(uuid.uuid4())
    User.objects.create(id=identifier)

    return identifier


def write_key(identifier, key, value):
    data = Data.objects.create(key=key, value=value)
    data.user = User.objects.get(id=identifier)
    if data:
        data.save()
    else:
        raise ValueError
    return data


def get_key(identifier, key):
    data = Data.objects.get(key=key, user=User.objects.get(id=identifier))
    if not data:
        raise ValueError

    return {"value": data.value}


def delete_key(identifier, key):
    data = Data.objects.get(key=key, user=User.objects.get(id=identifier))
    if not data:
        raise ValueError

    data.delete()
    return data
