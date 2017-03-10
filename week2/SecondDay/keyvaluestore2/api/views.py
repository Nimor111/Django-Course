from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .logic import create_user, write_key, get_key, delete_key
from .models import User, Data

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


def index_view(request):
    users_count = User.objects.count()
    keys_count = Data.objects.count()
    keys = Data.objects.all()

    histogram = {}

    for data in keys:
        if data.key not in histogram:
            histogram[data.key] = 1
        else:
            histogram[data.key] += 1

    users = User.objects.all()

    return render(request, 'index.html', locals())


def user_detail_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    # import ipdb; ipdb.set_trace()
    data = user.data_set.all()

    return render(request, 'user_detail.html', locals())


def add_key_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        store_key(user, key, value)

    return render(request, 'add_key.html', locals())
