from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

import django.contrib.auth.views as auth_views

from offer.views import register_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'website/login.html'},
        name='login'),
    url(r'logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'register/$', register_view, name='register'),
    url(r'^', include('offer.urls', namespace='offer')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
