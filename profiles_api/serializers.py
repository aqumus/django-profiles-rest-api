from dataclasses import fields
from rest_framework import serializers

from profiles_api.models import UserProfile, UserProfileStatusFeed

class HelloSerializer(serializers.Serializer):
    """Serializes name field for HelloAPIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=['id', 'email', 'name', 'password']
        extra_kwargs= {
            'password': {
                'write_only': True,
                'style': { 'input_type': 'password' }
            }
        }

    def create(self, validated_data):
        """Create and return a new userprofile"""
        user = UserProfile.objects.create_user(
            email= validated_data.get('email'),
            name= validated_data.get('name'),
            password= validated_data.get('password')
        )

        return user

    def update(self, instance, validated_data):
        """handle updating userprofile"""

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        return super().update(instance, validated_data)


class UserProfileStatusFeedSerializer(serializers.ModelSerializer):
    """Serializer for user profile feed model"""

    class Meta:
        model=UserProfileStatusFeed
        fields=('id', 'status_text', 'user_profile', 'created_on', 'modified_at')
        extra_kwargs = {
            'user_profile': { "read_only": True}
        }