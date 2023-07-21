from rest_framework.permissions import BasePermission

class UserPermissions(BasePermission):
    def has_permission(self, request, view):
        from flickr_user.api import UserDetailAPI
        
       ### Defines if the authentiates user  in request.user has permissions to do the action (GET,PUT,DELETE)
        if request.method == "POST":
           return True
        ##if not post the super user is always allowed
        elif request.user.is_superuser:
            return True
        ##if is get over the detail view i make the validation inside the has_object_permission method
        elif isinstance(view , UserDetailAPI):
            return True
        else:
            ## Get on /api/1.0/photos/
            return False

       
    def has_object_permission(self, request, view, obj):

         ### Defines if the authentiates user  in request.user has permissions to do the action (GET,PUT,DELETE) over the Object


         ## if superadmin , or the authenticated user try to do GET,PUT,DELETE over it's own profile
         return request.user.is_superuser or request.user==obj