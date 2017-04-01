import json
import uuid

from api.models import User, Data
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
    data = None
    if key not in list(map(lambda x: x.key, user.data_set.all())):
        data = Data.objects.create(key=key, value=value)
        data.user = user
        data.save()
    else:
        for d in user.data_set.all():
            if d.key == key:
                d.value = value
                d.save()
                break
    return data


def get_key(identifier, key):
    try:
        user = User.objects.get(pk=identifier)
    except Exception:
        raise ValueError

    res = None
    for d in user.data_set.all():
        if d.key == key:
            res = d
            break
    if res is None:
        raise KeyError

    return {"value": res.value}


def delete_key(identifier, key):
    try:
        user = User.objects.get(id=identifier)
    except Exception:
        raise ValueError

    res = None
    for d in user.data_set.all():
        if d.key == key:
            res = d
            res.delete()
            break
    if res is None:
        raise KeyError

    return res
