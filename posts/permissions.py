from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read only permissions are allowed for any request
        # SAFE_METHOS: tuple containing GET, OPTIONS and HEAD
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a post
        # Check if the author of the object in question (obj.author) matches the user
        # making the request request.user
        return obj.author == request.user
