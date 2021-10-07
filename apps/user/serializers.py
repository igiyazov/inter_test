from rest_framework import serializers

from apps.user.models import BaseUser

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser 
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )
        read_only_fields = fields