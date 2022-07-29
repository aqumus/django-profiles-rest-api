from rest_framework import permissions

class UpdateOwnUserProfile(permissions.BasePermission):
    """Check if user is trying to update their own user profile"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id