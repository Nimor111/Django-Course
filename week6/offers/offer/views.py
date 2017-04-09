from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, F

from django.views import generic

from .models import Offer, Category
from .forms import OfferModelForm

from moneyed import Money, EUR


class OfferListView(generic.ListView):
    model = Offer
    context_object_name = 'offers'
    template_name = 'website/index.html'

    def get_queryset(self):
        return Offer.objects.select_related('category', 'author').all()


class OfferCreateView(LoginRequiredMixin, generic.CreateView):
    model = Offer
    template_name = 'website/add_offer.html'
    login_url = reverse_lazy('login')
    form_class = OfferModelForm

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super(OfferCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('offer:index')

    def get_initial(self):
        return {'price': Money(100, EUR)}


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


def statistics_view(request):
    cat_stats = list(Offer.objects.values('category').annotate(name=F('category__name'), ccount=Count('category')).
                     order_by('-ccount'))[:3]

    return render(request, 'website/statistics.html', locals())
