from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.user.role == UserRoles.ADMIN:
            return True
        return False
