from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import Proyecto
from .forms import ProyectoForm

def index(request):
    return render(request, 'index.html')

def proyectos(request):
    proyectos = Proyecto.objects.all()

    if request.user.is_authenticated and request.user.is_profesor:
        if 'filtrar_patrocinados' in request.GET:
            proyectos = proyectos.filter(patrocinado=True)
        elif 'filtrar_no_patrocinados' in request.GET:
            proyectos = proyectos.filter(patrocinado=False)

    return render(request, 'proyectos.html', {'proyectos': proyectos})

@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.estudiante = request.user
            proyecto.save()
            return redirect('proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'crear_proyecto.html', {'form': form})

@login_required
def modificar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    if request.user == proyecto.estudiante or request.user.is_profesor:
        if request.method == 'POST':
            form = ProyectoForm(request.POST, instance=proyecto)
            if form.is_valid():
                form.save()
                return redirect('proyectos')
        else:
            form = ProyectoForm(instance=proyecto)
        return render(request, 'modificar_proyecto.html', {'form': form})
    else:
        return redirect('proyectos')

@login_required
def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    return render(request, 'detalle_proyecto.html', {'proyecto': proyecto})

@login_required
@user_passes_test(lambda u: u.is_profesor)
def patrocinar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    proyecto.patrocinador = request.user
    proyecto.patrocinado = True
    proyecto.save()
    return redirect('proyectos')



