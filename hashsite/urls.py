from django.contrib import admin
from django.urls import path, include

from .openapi import urlpatterns as doc


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(doc)),
    path('', include('apps.store.urls')),
    path('', include('apps.user.urls')),
]
