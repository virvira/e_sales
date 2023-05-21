from rest_framework.permissions import BasePermission


class IsActiveUserPermission(BasePermission):
    message = 'No access'

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False
