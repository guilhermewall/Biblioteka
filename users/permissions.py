from rest_framework import permissions
from users.models import User
from rest_framework.views import View


class IsCollaboratorOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        if request.user.is_authenticated and obj == request.user:
            return True

        if request.user.is_superuser:
            return True

        return False
