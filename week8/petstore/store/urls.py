from django.conf.urls import url
from store import views

urlpatterns = [
    url(r'^pet/$', views.pet, name='pet'),
]
