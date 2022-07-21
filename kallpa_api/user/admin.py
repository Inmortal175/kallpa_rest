from calendar import c
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
  fieldsets = (
    (None, {'fields': ('email','username', 'password')}),
    ("Estados", {'fields': ('is_active', 'is_staff', 'is_superuser', 'id_rol',)}),
    ('Permisos', {'fields': ('user_permissions',)}),
    ('Profile avatar', {'fields': ('profile',)}),
    ('information personal', {'fields': ('nombres', 'apellido_paterno', 'apellido_materno', 
    'documento_identidad', 'fecha_nac', 'celular', 'fecha_ingreso', )}),
  )
  readonly_fields = ('fecha_ingreso',)