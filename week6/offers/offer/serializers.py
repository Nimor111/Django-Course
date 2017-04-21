from rest_framework import serializers
from offer.models import Offer, Category


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('title', 'price', 'description',
                  'image', 'status', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')
