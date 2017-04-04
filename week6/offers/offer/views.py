from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Offer
from .forms import OfferModelForm


# Create your views here.
def index_view(request):
    offers = Offer.objects.select_related('category', 'author').all()

    return render(request, 'website/index.html', locals())


def offer_create_view(request):
    form = OfferModelForm()

    if request.method == 'POST':
        form = OfferModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('offer:index'))

    return render(request, 'website/add_offer.html', locals())
