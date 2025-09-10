from rest_framework import viewsets, status
from rest_framework.response import Response
from ecommerce.models.delivery_service_provider import DeliveryServiceProvider
from ecommerce.serializers.delivery_service_provider import DeliveryServiceProviderSerializer
from rest_framework.permissions import AllowAny

class DeliveryServiceProviderViewSet(viewsets.ModelViewSet):
    queryset = DeliveryServiceProvider.objects.all()
    serializer_class = DeliveryServiceProviderSerializer
    permission_classes = [AllowAny]

    # Thêm dòng này
    required_alternate_scopes = {
        'create': [['delivery_service_provider:write']],
        'list': [['delivery_service_provider:read']],
        'retrieve': [['delivery_service_provider:read']],
        'update': [['delivery_service_provider:write']],
        'partial_update': [['delivery_service_provider:write']],
        'destroy': [['delivery_service_provider:write']],
    }

    def create(self, request, *args, **kwargs):
        print("Request reached ViewSet!")  # debug
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        print("Saved instance:", instance)
        return Response(
            DeliveryServiceProviderSerializer(instance).data,
            status=status.HTTP_201_CREATED
        )
