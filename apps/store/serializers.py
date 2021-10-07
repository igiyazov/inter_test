from rest_framework import fields, serializers

from apps.store.models import Consumer, Store

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
        extra_fields = {
            'hash': {'read_only': True},
        }

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = '__all__'
        extra_fields = {
            'hash': {'read_only': True},
        }

class ReadOnlyIdsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    
# class PurchaseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Purchase
#         exclude = ('hash',)