from rest_framework import permissions
from rest_framework.views import View, Request
from users.models import User


class IsCollaboratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, req: Request, view: View) -> bool:
        return (
            req.user.is_authenticated
            and req.method in permissions.SAFE_METHODS
            or req.user.is_collaborator
        )


class IsColaborator(permissions.BasePermission):
    def has_permission(self, req: Request, view: View) -> bool:
        return req.user.is_authenticated and req.user.is_collaborator


class IsAdmAuthentication(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        return request.user.is_superuser and request.user.is_authenticated

