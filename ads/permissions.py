from django.http import Http404
from rest_framework import permissions

from ads.models import Selection, Ad
from user.models import User


class SelectionUpdatePermission(permissions.BasePermission):
    message = 'Permission denied'

    def has_permission(self, request, view):
        try:
            selection = Selection.objects.get(pk=view.kwargs["pk"])
        except Selection.DoesNotExist:
            raise Http404

        if selection.owner.id == request.user.id:
            return True
        else:
            return False


class AdUpdatePermission(permissions.BasePermission):
    message = 'Permission denied'

    def has_permission(self, request, view):
        if request.user.role in [User.MODERATOR, User.ADMIN]:
            return True

        try:
            ad = Ad.objects.get(pk=view.kwargs["pk"])
        except Ad.DoesNotExist:
            raise Http404

        if ad.author_id == request.user.id:
            return True
        return False
