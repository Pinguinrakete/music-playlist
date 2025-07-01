from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated

 # alle dürfen GET | nur staff oder wenn authenticated dürfen POST 
class allCanGETButStaffOrAuthenticatedOnlyPOST(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and (request.user.is_staff or request.user.is_authenticated)