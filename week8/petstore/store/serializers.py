from rest_framework import serializers
from store.models import Pet


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pet
        fields = ("name", "age")
