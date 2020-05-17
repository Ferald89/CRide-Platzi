"""Circle permissions classes. """

# Django REST Framework
from rest_framework.permissions import BasePermission

# Model
from cride.circles.models import Membership


class IsActiveCircleMember(BasePermission):
    """Allow acess only to circle members.
    Expect taht the views implementing this permission
    have a circle atribute assigned.
    """
    def has_permission(self, request, view):
        """Verify user in an active member of the circle"""
        try:
            Membership.objects.get(
                      user=request.user,
                      circle=view.circle,
                      is_active=True
                      )
        except Membership.DoesNotExist:
            return False
        return True


class IsSelfMember(BasePermission):
    """Allow acces only to member owner."""

    def has_permission(self, request, view):
        """Let object permission gran acess. """
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)

    def has_object_permission(self, request, view, obj):
        """Allow acces only if member is owned by the requesting user."""
        return request.user == obj.user
