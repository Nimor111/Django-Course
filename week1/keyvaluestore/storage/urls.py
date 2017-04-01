from django.conf.urls import url

from . import views

uuid_regex = '([a-zA-Z]|[0-9]){8}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){4}\-([a-zA-Z]|[0-9]){12}'


urlpatterns = [
    url(r'^create-user/', views.create_user_view, name='create'),
    url(r'^(?P<useridentifier>{})/$'.format(uuid_regex),
        views.write_key_view, name='store'),
    url(r'^(?P<useridentifier>{})/(?P<key>[A-Za-z0-9]+)/$'.format(uuid_regex),
        views.get_or_delete_view, name='get_key'),
]
