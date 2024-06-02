from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Profesor, Estudiante, Proyecto

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('is_profesor', 'is_estudiante')

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre_proyecto', 'tema', 'nombre_profesor', 'descripcion', 'patrocinado', 'profesor_patrocinador']  # Añadimos los nuevos campos
