from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.post_list_view, name='index'),
    url(r'^post/(?P<pk>[0-9]+)', views.post_detail_view, name='post_detail'),
]
