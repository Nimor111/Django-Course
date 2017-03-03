import json
import uuid
import glob

from django.conf import settings


def create_user():
    identifier = str(uuid.uuid4())
    with open('{}/{}.json'.format(settings.JSON_DATABASE,
              identifier), 'w') as fp:
        fp.write(json.dumps({}))

    return identifier


def write_key(identifier, key, value):
    files = glob.glob('proto_db/*.json')
    path = 'proto_db/' + identifier + '.json'
    if path not in files:
        raise FileNotFoundError

    with open(path, 'r') as fp:
        data = json.load(fp)
        data[key] = value

    with open(path, 'w') as fp:
        fp.write(json.dumps(data, indent=4))

    return True


def get_key(identifier, key):
    files = glob.glob('proto_db/*.json')
    path = 'proto_db/' + identifier + '.json'
    if path not in files:
        raise FileNotFoundError

    with open(path, 'r') as fp:
        data = json.load(fp)
        if key not in list(data.keys()):
            raise ValueError
        value = data.get(key)

    return {"value": value}


def delete_key(identifier, key):
    files = glob.glob('proto_db/*.json')
    path = 'proto_db/' + identifier + '.json'
    if path not in files:
        raise FileNotFoundError

    with open(path, 'r') as fp:
        data = json.load(fp)
        if key not in list(data.keys()):
            raise ValueError
        data.pop(key)

    with open(path, 'w') as fp:
        fp.write(json.dumps(data, indent=4))

    return data
