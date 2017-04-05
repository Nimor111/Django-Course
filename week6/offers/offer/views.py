from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from .models import Offer, Category
from .forms import OfferModelForm


def index_view(request):
    offers = Offer.objects.select_related('category', 'author').all()
    categories = Category.objects.all()

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


def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            form.save()
            return redirect(reverse_lazy('offer:index'))
        else:
            return redirect('/register/')
    return render(request, 'website/register.html', locals())
