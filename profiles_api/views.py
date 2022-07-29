from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import permissions, serializers
from profiles_api.models import UserProfile, UserProfileStatusFeed


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


class HelloViewSet(viewsets.ViewSet):
    """Viewset API methods"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
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

    def create(self, request):
        """Create a create object"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            return Response({
                "message": f'Hello {name}'
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle retrieving a object using id"""
        return Response({
            "message": "Retrieved an object"
        })

    def update(self, request, pk=None):
        """Handle updating a object using id"""
        return Response({
            "message": "Updated an object"
        })

    def partial_update(self, request, pk=None):
        """Handle partial updating a object using id"""
        return Response({
            "message": "Partially updated an object"
        })

    def destroy(self, request, pk=None):
        """Handle deleting a object using id"""
        return Response({
            "message": "Deleted an object"
        })


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnUserProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email', )


class UserLoginApiView(ObtainAuthToken):
    """User login view"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileStatusFeedViewSet(viewsets.ModelViewSet):
    """View set for UserProfile status feed API"""

    authentication_classes= (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, permissions.UpdateOwnUserStatus, )
    serializer_class = serializers.UserProfileStatusFeedSerializer
    queryset = UserProfileStatusFeed.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
