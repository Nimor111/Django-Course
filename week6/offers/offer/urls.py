from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.OfferListView.as_view(), name='index'),
    url(r'^add-offer/$', views.OfferCreateView.as_view(), name='offer-create'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.OfferCategoryListView.as_view(), name='category'),
    url(r'^statistics/$', views.StatisticsView.as_view(), name='statistics'),
]
