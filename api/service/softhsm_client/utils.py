from rest_framework.permissions import BasePermission


class AllowAll(BasePermission):
    """
    Dummy permisiion implementation
    """

    def has_permission(self, request, view):
        return True
