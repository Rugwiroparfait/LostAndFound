from rest_framework import serializers
from .models import Claim

class ClaimSerializer(serializers.ModelSerializer):
    """
    Serializer for the claim model.

    This serializer maps the Claim model fields to JSON format and handles
    validation, creation, and updates of Claim instances.
    """
    class Meta:
        model = Claim
        fields = [
            'id',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']