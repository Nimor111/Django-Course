import uuid
import json

from django.http import HttpResponse, JsonResponse
from .logic import create_user, write_key, get_key, delete_key
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def create_user_view(_):
    identifier = create_user()
    # import ipdb; ipdb.set_trace()
    data = {'identifier': identifier}
    return JsonResponse(data, json_dumps_params={'indent': 4})


@csrf_exempt
def write_key_view(request, useridentifier):
    if request.method == 'POST':
        body = request.body.decode('utf-8')
        body = json.loads(body)
        if body is not None:
            try:
                write_key(useridentifier, body['key'], body['value'])
            except FileNotFoundError:
                error = {
                    "error": "User not found!"
                }
                return JsonResponse(error, json_dumps_params={'indent': 4},
                                    status=404)
            return HttpResponse(status=201)
    return HttpResponse(status=403)


@csrf_exempt
def get_or_delete_view(request, useridentifier, key):
    if request.method == 'GET':
        return get_key_view(request, useridentifier, key)
    if request.method == 'DELETE':
        return delete_key_view(request, useridentifier, key)


@csrf_exempt
def get_key_view(request, useridentifier, key):
    try:
        data = get_key(useridentifier, key)
        return JsonResponse(data, json_dumps_params={'indent': 4},
                            status=200)
    except FileNotFoundError:
        return JsonResponse({"error": "File not found."},
                            json_dumps_params={'indent': 4},
                            status=404)
    except ValueError:
        return JsonResponse({"error": "Key not found."},
                            json_dumps_params={'indent': 4},
                            status=404)


@csrf_exempt
def delete_key_view(request, useridentifier, key):
    try:
        data = delete_key(useridentifier, key)
        return JsonResponse({"status": "deleted"}, status=202)
    except FileNotFoundError:
        return JsonResponse({"error": "File not found."}, status=404)
    except ValueError:
        return JsonResponse({"error": "Key not found."}, status=404)
