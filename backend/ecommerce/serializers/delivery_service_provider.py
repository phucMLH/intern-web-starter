from rest_framework import serializers
from ecommerce.models.delivery_service_provider import DeliveryServiceProvider

class DeliveryServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryServiceProvider
        fields = "__all__"
