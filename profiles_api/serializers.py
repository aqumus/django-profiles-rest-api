from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes name field for HelloAPIView"""
    name = serializers.CharField(max_length=10)