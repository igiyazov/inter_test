from django.shortcuts import render
from rest_framework import filters, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from apps.store.models import Store, Consumer
from apps.store.serializers import ReadOnlyIdsSerializer, StoreSerializer, ConsumerSerializer

class StoreView(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter] #Первый способ поиска
    search_fields = ['hash']
    

class ConsumerView(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer
    permission_classes = [permissions.AllowAny]


    @swagger_auto_schema(
        method='get', 
        manual_parameters=[
            openapi.Parameter(
                'search',
                openapi.IN_QUERY,
                description="Search object by hash",
                type=openapi.TYPE_STRING,
            )
        ], 
        responses={200: openapi.Response('Searched', ReadOnlyIdsSerializer)},
    )
    @action(
        methods=['get'],
        detail=False,
        url_path='search',
        url_name='search-by-hash',
        serializer_class=ReadOnlyIdsSerializer,
    )
    def search_by_hash(self, request, *args, **kwargs): # Второй способ поиска
        search_text = request.query_params.get('search')
        data = Consumer.search_by_hash(search_text)
        serialized = self.get_serializer(data, many=True)
        return Response(serialized.data)


 