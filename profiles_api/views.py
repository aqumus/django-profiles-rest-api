from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test API View"""

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