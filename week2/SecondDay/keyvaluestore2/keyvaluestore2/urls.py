from django.conf.urls import url, include
from django.contrib import admin

from api import views

uuid_regex = '([a-zA-Z]|[0-9]){8}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){12}'

urlpatterns = [
    url(r'^api/storage/', include('api.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index_view, name='index'),
    url(r'^user-detail/(?P<user_id>{})/$'.format(uuid_regex),
        views.user_detail_view, name='user_detail'),
    url(r'^add-key/(?P<user_id>{})/$'.format(uuid_regex),
        views.add_key_view, name='add_key'),
]
