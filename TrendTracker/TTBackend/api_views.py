from django.core.files.base import ContentFile
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework import viewsets, mixins, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions class
class UserPermissions(permissions.AllowAny):
    def has_permission(self, request, view):
        for perm, actions in getattr(view, "perms", {}).items():
            if view.action in actions:
                return perm().has_permission(request, view)
        return False
