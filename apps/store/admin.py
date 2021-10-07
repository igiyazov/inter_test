from django.contrib import admin

from apps.store.models import Consumer, Store

admin.site.register(Store)
admin.site.register(Consumer)