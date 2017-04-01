from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .logic import create_user, write_key, get_key, delete_key

import json


# Create your views here.
@csrf_exempt
def create_user_view(request):
    identifier = create_user()
    return JsonResponse({'identifier': identifier})


@csrf_exempt
def write_key_view(request, identifier):
    if request.method == 'POST':
        body = request.body.decode('utf-8')
        body = json.loads(body)
        try:
            write_key(identifier, body['key'], body['value'])
            return HttpResponse(status=201)
        except ValueError:
            return HttpResponse(status=404)
    return HttpResponse(status=403)


@csrf_exempt
def get_or_delete_view(request, identifier, key):
    if request.method == 'GET':
        return get_key_view(request, identifier, key)
    if request.method == 'DELETE':
        return delete_key_view(request, identifier, key)


@csrf_exempt
def get_key_view(_, identifier, key):
    try:
        data = get_key(identifier, key)
        return JsonResponse(data, json_dumps_params={'indent': 4}, status=200)
    except KeyError:
        return JsonResponse({"error": "Key not found."},
                            json_dumps_params={'indent': 4},
                            status=404)
    except ValueError:
        return JsonResponse({"error": "Key not found."},
                            json_dumps_params={'indent': 4},
                            status=404)


@csrf_exempt
def delete_key_view(_, identifier, key):
    try:
        data = delete_key(identifier, key)
        return JsonResponse({'status': 'deleted'}, status=202)
    except KeyError:
        return JsonResponse({'error': 'key'}, status=404)
    except ValueError:
        return JsonResponse({"error": "Key not found."},
                            json_dumps_params={'indent': 4},
                            status=404)
