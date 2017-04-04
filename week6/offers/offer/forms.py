from django import forms

from .models import Offer


class OfferModelForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('title', 'price', 'description', 'image', 'category')
