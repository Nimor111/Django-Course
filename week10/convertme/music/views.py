from django.shortcuts import render

from django.views import generic
from django.urls import reverse_lazy

from celery import chain

from .forms import SongModelForm
from .tasks import chain_tasks


class IndexView(generic.CreateView):
    template_name = 'website/index.html'
    form_class = SongModelForm
    success_url = reverse_lazy('music:index')

    def form_valid(self, form):
        chain_tasks(form.cleaned_data['link'], form.cleaned_data['email']).apply_async()
        return super().form_valid(form)
