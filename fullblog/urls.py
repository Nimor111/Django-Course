from django.conf.urls import url, include
from django.contrib import admin

import .settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls', namespace='blog')),
]
