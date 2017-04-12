from django import forms

from .models import Offer


class OfferModelForm(forms.ModelForm):
    use_required_attribute = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['price'].required = False
        self.fields['title'].required = False
        self.fields['description'].required = False
        self.fields['status'].required = False

    class Meta:
        model = Offer
        fields = ('title', 'price', 'status', 'description', 'image', 'category')
        widgets = {'status': forms.HiddenInput()}
