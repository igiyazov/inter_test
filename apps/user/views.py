from rest_framework import viewsets


from apps.user.models import BaseUser
from apps.user.serializers import BaseUserSerializer


class BaseUserView(viewsets.ReadOnlyModelViewSet):
    queryset = BaseUser.objects.all()
    serializer_class = BaseUserSerializer
    



