from django.conf.urls import url

import music.views as views


urlpatterns = [
    url(r'^', views.IndexView.as_view(), name='index'),
]
