from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Custom permission that allows only task owners to view or edit their tasks.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
