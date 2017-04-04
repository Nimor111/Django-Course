from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^add-offer', views.offer_create_view, name='offer-create'),
]
