from django.urls.conf import include, path
from rest_framework.routers import DefaultRouter

from apps.store.views import ConsumerView, StoreView

router = DefaultRouter()
router.register('store', StoreView)
router.register('consumer', ConsumerView)

urlpatterns = [
    path('', include(router.urls))
]