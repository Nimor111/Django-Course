from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index_view(request):
    return render(request, 'website/home-blog-v4.html', locals())
