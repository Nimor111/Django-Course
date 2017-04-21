from django.shortcuts import render
from django.http import JsonResponse
from store.models import Pet
from store.serializers import PetSerializer


# Create your views here.
def pet(request):
    pets = Pet.objects.all()
    serializer = PetSerializer(pets, many=True)

    return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 4})
