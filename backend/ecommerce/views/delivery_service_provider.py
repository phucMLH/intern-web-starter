from rest_framework import viewsets
from ecommerce.models.delivery_service_provider import DeliveryServiceProvider
from ecommerce.serializers.delivery_service_provider import DeliveryServiceProviderSerializer

class DeliveryServiceProviderViewSet(viewsets.ModelViewSet):
    queryset = DeliveryServiceProvider.objects.all()
    serializer_class = DeliveryServiceProviderSerializer
