from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from .models import Offer, Category
from .forms import OfferModelForm


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


def offer_category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    offers = Offer.objects.filter(category=category)

    return render(request, 'website/offers_by_category.html', locals())
