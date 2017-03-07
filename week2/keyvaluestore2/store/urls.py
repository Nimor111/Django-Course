from django.conf.urls import url

from . import views


uuid_regex = '([a-zA-Z]|[0-9]){8}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){12}'


urlpatterns = [
    url(r'^create-user/$', views.create_user_view, name='create_user'),
    url(r'(?P<identifier>{})/$'.format(uuid_regex), views.write_key_view,
        name='write_key'),
]
