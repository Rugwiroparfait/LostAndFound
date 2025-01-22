from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the Item model.

    this serializer maps the Item model fields to JSON format and handles
    validation, creation, and updates of Item instances.
    """
    class Meta:
        model = Item
        fields = [
            'id',
            'title',
            'description',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']