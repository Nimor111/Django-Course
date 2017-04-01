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
    try:
        user = User.objects.get(pk=identifier)
    except Exception:
        raise ValueError
    data = Data.objects.create(key=key, value=value)
    user.key = data
    user.save()
    data.save()
    return data


def get_key(identifier, key):
    try:
        user = User.objects.get(pk=identifier)
    except Exception:
        raise ValueError

    try:
        key_data = Data.objects.filter(key=key)
        for d in key_data:
            if user in d.user_set.all():
                key_data = d
        if not isinstance(key_data, Data):
            raise ValueError
    except Exception:
        raise KeyError

    return {"value": key_data.value}


def delete_key(identifier, key):
    try:
        user = User.objects.get(id=identifier)
    except Exception:
        raise ValueError
    try:
        key_data = Data.objects.filter(key=key)
        for d in key_data:
            if user in d.user_set.all():
                key_data = d
        if not isinstance(key_data, Data):
            raise ValueError

        key_data.delete()
    except Exception:
        raise KeyError

    return key_data
