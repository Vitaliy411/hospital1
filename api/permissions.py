from rest_framework import permissions

class DoctorAccessPermissions(permissions.BasePermission):

    def has_permission(self, request, view):

        return 'api.view_doctor' in request.user.get_user_permissions()

