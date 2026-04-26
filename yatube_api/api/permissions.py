from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.IsAuthenticated):
    """Разрешает изменение/удаление только автору объекта."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
