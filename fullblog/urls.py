from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth import views as auth_views
from blog.views import register_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('blog.urls', namespace='blog')),
    url(r'^login/$', auth_views.login, {'template_name': 'website/page-user-login-classic.html'},
        name='login'),
    url(r'logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'register/$', register_view, name='register'),
]
