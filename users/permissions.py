from rest_framework import permissions


class OnlyStaffOwnerUserPermission(permissions.BasePermission):
    """
    Custom user API permissions.

    - Normal users can't send requests
    - Staff and Owner can do everything

    """

    message = 'Only Staff or Owner Users can access this endpoint.'

    def has_permission(self, request, view):
        if request.user.is_staff or request.user.is_superuser:
            return True
        else:
            return False

        return request.user.is_authenticated

class OnlyAdminOwnerUserPermission(permissions.BasePermission):
    """
    Custom user API permissions.

    - Normal users can't send requests
    - Staff, Investor and Owner can do everything

    """

    message = 'Only Admin Staff or Owner Users can access this endpoint.'

    def has_permission(self, request, view):
        if request.user.level == 2 or request.user.is_superuser:
            return True
        else:
            return False

        return request.user.is_authenticated

class OnlyInvestorOwnerUserPermission(permissions.BasePermission):
    """
    Custom user API permissions.

    - Normal users can't send requests
    - Investor and Owners can do everything

    """
    message = 'Only Investors or Owners can access this endpoint.'

    def has_permission(self, request, view):
        if request.user.is_superuser and request.user.level == 1:
            return True
        else:
            return False

        return request.user.is_authenticated

class OnlyOwnerUserPermission(permissions.BasePermission):
    """
    Custom user API permissions.

    - Normal users can't send requests
    - Staff and Superusers can do everything

    """

    message = 'Only Owners can access this endpoint.'

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            return False

        return request.user.is_authenticated