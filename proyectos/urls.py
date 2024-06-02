#Patrones para urlresolver
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('proyecto/<int:proyecto_id>/', views.detalle_proyecto, name='detalle_proyecto'),
    path('crear/', views.crear_proyecto, name='crear_proyecto'),
    path('modificar/<int:proyecto_id>/', views.modificar_proyecto, name='modificar_proyecto'),
    path('patrocinar/<int:proyecto_id>/', views.patrocinar_proyecto, name='patrocinar_proyecto'),
]
