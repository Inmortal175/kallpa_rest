import re
from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
  def has_permission(self, request, view):
    if request.method == 'GET':
      return True
    else:
      return request.user.is_staff

class IsClient(BasePermission):
  def has_permission(self, request, view):
    return str(request.user.id_rol) == str(3)

class IsDistribuidor(BasePermission):
  def has_permission(self, request, view):
    return str(request.user.id_rol) == str(2)