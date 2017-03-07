from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .logic import create_user, write_key
from .models import User

import json


# Create your views here.
@csrf_exempt
def create_user_view(request):
    identifier = create_user()
    return JsonResponse({'identifier': identifier})


@csrf_exempt
def write_key_view(request, identifier):
    if User.objects.filter(id=identifier):
        if request.method == 'POST':
            body = request.body.decode('utf-8')
            body = json.loads(body)
            write_key(identifier, body['key'], body['value'])
            return HttpResponse(status=201)
        return HttpResponse(status=403)
    else:
        return HttpResponse(status=404)
