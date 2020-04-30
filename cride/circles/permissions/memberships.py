"""Circle permissions classes. """

#Django REST Framework
from rest_framework.permissions import BasePermission

#Model
from cride.circles.models import Membership


class IsActiveCircleMember(BasePermission):
  """Allow acess only to circle members.
  Expect taht the views implementing this permission
  have a circle atribute assigned.
  """
  def has_permission(self,request,view):
    """Verify user in an active member of the circle"""
    circle = view.circle
    try:
      Membership.objects.get(
        user=request.user,
        circle=view.circle,
        is_active=True
      )
    except Membership.DoesNotExist:
      return False
    return True



