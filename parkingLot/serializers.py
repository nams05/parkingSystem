from rest_framework import serializers
from .models import *


# class CarDetailsSerializer(serializers.ModelSerializer):
#     """Serializer to map the Model instance into JSON format."""
#
#     class Meta:
#         """Meta class to map serializer's fields with the model fields."""
#         model = CarDetails
#         fields = ('id', 'registration_number', 'color', 'created_on', 'updated_at')
#         read_only_fields = ('created_on', 'updated_at')


class SlotDetailsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = SlotDetails
        fields = ('id', 'registration_number', 'color', 'created_on', 'updated_at')
        read_only_fields = ('created_on', 'updated_at')
