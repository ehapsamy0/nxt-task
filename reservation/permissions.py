from rest_framework import permissions




class IsCreateOrIsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.method == "POST":
            return True
        return bool(request.user and request.user.is_superuser)
