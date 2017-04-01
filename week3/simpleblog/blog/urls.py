from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index_view, name='index_view'),
    url(r'^(?P<pk>[0-9]+)', views.post_detail_view, name='detail_view'),
    url(r'^add/$', views.add_post_view, name='add_post'),
]
