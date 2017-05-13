from rest_framework import permissions
from src.common.libraries.constants import *

class IsAuthenticatedOrCreate(permissions.BasePermission):
    SAFE_METHODS = [HTTP_METHOD_POST]
    def has_permission(self, request, view):
        return ( request.method in IsAuthenticatedOrCreate.SAFE_METHODS or request.user and request.user.is_authenticated() )

class IsStaffOrIsAuthenticatedForReadUpdate(permissions.BasePermission):
    SAFE_METHODS = []
    AUTH_METHODS = [HTTP_METHOD_GET, HTTP_METHOD_PUT]
    STAFF_METHOD = [HTTP_METHOD_DELETE, HTTP_METHOD_POST]
    def has_permission(self, request, view):
        if request.method in IsStaffOrIsAuthenticatedForReadUpdate.AUTH_METHODS:
            return (
                request.method in IsStaffOrIsAuthenticatedForReadUpdate.SAFE_METHODS
                or request.user
                and request.user.is_authenticated()
            )
        elif request.method in IsStaffOrIsAuthenticatedForReadUpdate.STAFF_METHOD:
            return (
                request.method in IsStaffOrIsAuthenticatedForReadUpdate.SAFE_METHODS
                or request.user
                and request.user.is_staff
            )

class IsAdminUser(permissions.BasePermission):
    SAFE_METHODS = []
    def has_permission(self, request, view):
        return ( request.method in IsAdminUser.SAFE_METHODS or request.user and request.user.is_admin )

class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return ( request.user and request.user.is_authenticated() )




