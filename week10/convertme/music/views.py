from django.shortcuts import render

from django.views import generic
from django.urls import reverse_lazy

from celery import chain

from .forms import SongModelForm
from .tasks import download_url, convert_mp4


# Create your views here.
class IndexView(generic.CreateView):
    template_name = 'website/index.html'
    form_class = SongModelForm
    success_url = reverse_lazy('music:index')

    def form_valid(self, form):
        chain(download_url.s(form.cleaned_data.get('link')), convert_mp4.s()).apply_async()
        return super().form_valid(form)
