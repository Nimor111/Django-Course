from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.OfferListView.as_view(), name='index'),
    url(r'^add-offer/$', views.OfferCreateView.as_view(), name='offer-create'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.OfferCategoryListView.as_view(), name='category'),
    url(r'^offer/(?P<pk>[0-9]+)/$', views.OfferDetailView.as_view(), name='offer-detail'),
    url(r'^statistics/$', views.StatisticsView.as_view(), name='statistics'),
    url(r'^offer/edit/(?P<pk>[0-9]+)', views.OfferUpdateView.as_view(), name='offer-update'),
    url(r'^delete/(?P<pk>[0-9]+)', views.OfferDeleteView.as_view(), name='offer-delete'),
    url(r'^pending/$', views.PendingOffersView.as_view(), name='pending'),
    url(r'^accept/(?P<pk>[0-9]+)', views.OfferAcceptStatusView.as_view(), name='offer-accept'),
    url(r'^user/(?P<pk>[0-9]+)', views.ApprovedAndRejectedOffersView.as_view(), name='user-offers'),
    url(r'^reject/(?P<pk>[0-9]+)', views.OfferRejectStatusView.as_view(), name='offer-reject')
]
