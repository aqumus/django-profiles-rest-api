from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloAPIView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return list of API Views"""
        sample_data = [
            "Apple",
            "Banana",
            "Strawberry",
            "Water Melon"
        ]

        return Response({
            "sample":  sample_data
        })

    def post(self, request):
        """Create a API View object"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({
                "message": message
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Update object"""
        return Response({"message": "PUT successful"})

    def patch(self, request, pk=None):
        """Update partial object"""
        return Response({"message": "PATCH successful"})
    
    def delete(self, request, pk=None):
        """Delete a object"""
        return Response({"message": "DELETE successful"})