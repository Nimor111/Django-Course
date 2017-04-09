from django import forms

from .models import Offer


class OfferModelForm(forms.ModelForm):
    use_required_attribute = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['price'].required = False

    class Meta:
        model = Offer
        fields = ('title', 'price', 'description', 'image', 'category')
