from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profesor, Estudiante, Proyecto

#Definicion de la clase Administrador personalizada
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_profesor', 'is_estudiante')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Proyecto)