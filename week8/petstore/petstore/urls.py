from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('store.urls', namespace='store')),
    url(r'^admin/', admin.site.urls),
]
