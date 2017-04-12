from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count, F

from django.views import generic

from .models import Offer, Category
from .forms import OfferModelForm
from .mixins import CanUpdateOfferMixin, IsSuperUserMixin

from moneyed import Money, EUR


class OfferListView(generic.ListView):
    model = Offer
    context_object_name = 'offers'
    template_name = 'website/index.html'

    def get_queryset(self):
        return Offer.objects.get_accepted_offers()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.all()

        return context


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


class OfferCategoryListView(LoginRequiredMixin, generic.ListView):
    model = Offer
    template_name = 'website/offers_by_category.html'
    context_object_name = 'offers'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Offer.objects.filter(category=category)


class StatisticsView(generic.TemplateView):
    template_name = 'website/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cat_stats'] = list(Offer.objects.values('category').annotate(name=F('category__name'), ccount=Count('category')).order_by('-ccount'))[:3]

        return context


class OfferDetailView(LoginRequiredMixin, generic.DetailView):
    model = Offer
    login_url = reverse_lazy('login')
    template_name = 'website/offer_detail.html'
    context_object_name = 'offer'

    def get_object(self):
        return get_object_or_404(Offer, pk=self.kwargs['pk'])


class OfferUpdateView(LoginRequiredMixin, CanUpdateOfferMixin,
                      generic.UpdateView):
    model = Offer
    login_url = reverse_lazy('login')
    template_name = 'website/add_offer.html'
    form_class = OfferModelForm

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super(OfferUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('offer:index')


class OfferDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Offer
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse_lazy('offer:index')


class PendingOffersView(LoginRequiredMixin, IsSuperUserMixin, generic.ListView):
    model = Offer
    template_name = 'website/index.html'
    context_object_name = 'offers'

    def get_queryset(self):
        return Offer.objects.get_pending_offers()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pending'] = True

        return context


class OfferAcceptStatusView(LoginRequiredMixin, IsSuperUserMixin, generic.UpdateView):
    model = Offer
    login_url = reverse_lazy('login')
    template_name = 'website/index.html'
    form_class = OfferModelForm

    def form_valid(self, form):
        form.instance = Offer.objects.get(pk=self.kwargs['pk'])
        # import ipdb; ipdb.set_trace()
        form.instance.status = "a"

        return super(OfferAcceptStatusView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('offer:index')


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
