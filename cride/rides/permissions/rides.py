"""Rides permissions. """

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsRideOwner(BasePermission):
  """Verify requestin user is the ride create."""
  def has_object_permission(self,request,view,obj):
    """Verify requestering user is the ride creator."""
    return request.user == obj.offered_by

class IsNotRideOwner(BasePermission):
  """Verify teqestin user is not ride create. """
  def has_object_permission(self,request,view,obj):
    """Verify requestering user is the ride creator."""
    return not request.user == obj.offered_by
    # return True