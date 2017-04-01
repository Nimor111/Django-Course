from django.shortcuts import render
from django.http import HttpResponse

import json


# Create your views here.
def add(request, a, b):
    format = request.GET.get('format', ' ')
    data = int(a) + int(b)
    if format.lower() == 'json':
        data = {
            'result': int(a) + int(b)
        }

    response = HttpResponse(json.dumps(data, indent=4))
    response['Content-Type'] = 'application/json'
    return response


def multiply(request, a, b):
    data = int(a) * int(b)
    format = request.GET.get('format', ' ')
    if format.lower() == 'json':
        data = {
            'result': int(a) * int(b)
        }

    response = HttpResponse(json.dumps(data, indent=4))
    response['Content-Type'] = 'application/json'
    return response


def power(request, a, b):
    res = 1
    for i in range(int(b)):
        res *= int(a)
    format = request.GET.get('format', ' ')
    data = res
    if format.lower() == 'json':
        data = {
            'result': res
        }

    response = HttpResponse(json.dumps(data, indent=4))
    response['Content-Type'] = 'application/json'
    return response


def fact(request, n):
    f = 1
    for i in range(1, int(n) + 1):
        f *= i
    format = request.GET.get('format', ' ')
    data = f
    if format.lower() == 'json':
        data = {
            'result': f
        }

    response = HttpResponse(json.dumps(data, indent=4))
    response['Content-Type'] = 'application/json'
    return response
