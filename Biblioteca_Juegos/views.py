from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    form = BusquedaForm()
    return render(request, 'Biblioteca_Juegos/home.html', {'form': form})

@login_required
def administrar(request):
    return render(request, 'Biblioteca_Juegos/administrar.html')

def acerca(request):
    return render(request, 'Biblioteca_Juegos/acerca.html')

def agregar_juegos(request):
    mensaje = ""
    if request.method == "POST":
        pc_form = JuegoNvoForm(request.POST, request.FILES, prefix="nvojuego")
        if pc_form.is_valid():
            pc_form.save()
            mensaje = "Juego guardado correctamente."
            pc_form = JuegoNvoForm()  # limpia el formulario
    else:
        pc_form = JuegoNvoForm(prefix="nvojuego")

    return render(request, 'Biblioteca_Juegos/agregar_juego.html', {
        'pc_form': pc_form,
        'mensaje': mensaje
    })

def buscar_juego(request):
    resultados = []
    if request.method == "GET":
        form = BusquedaForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            resultados = JuegoNvo.objects.filter(nombre__icontains=nombre)
    return render(request, 'Biblioteca_Juegos/resultados_busqueda.html', {'resultados': resultados})

def listar_juegos(request):
    juegos = JuegoNvo.objects.all()
    return render(request, 'Biblioteca_Juegos/listar_juegos.html', {'juegos': juegos})

class JuegoListView(LoginRequiredMixin, ListView):
    model = JuegoNvo
    template_name = 'Biblioteca_Juegos/listar_juegos.html'
    context_object_name = 'juegos'

def ver_juego(request, id):
    juego = JuegoNvo.objects.get(id=id)
    resultados = [juego]
    return render(request, 'Biblioteca_Juegos/resultados_busqueda.html', {'resultados': resultados})

def editar_juego(request, id):
    juego = JuegoNvo.objects.get(id=id)
    if request.method == 'POST':
        form = JuegoNvoForm(request.POST, request.FILES, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('listar_juegos')
    else:
        form = JuegoNvoForm(instance=juego)
    return render(request, 'Biblioteca_Juegos/agregar_juego.html', {'pc_form': form, 'mensaje': 'Editando juego'})

def borrar_juego(request, id):
    juego = JuegoNvo.objects.get(id=id)
    juego.delete()
    return redirect('listar_juegos')

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if not hasattr(user, 'avatar'):
                return redirect('agregar_avatar')
            return redirect('home')
    else:
        form = UserLoginForm()

    return render(request, 'Biblioteca_Juegos/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


def registro_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'Biblioteca_Juegos/agregar_usuario.html', {'form': form})

User = get_user_model()
@login_required
def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'Biblioteca_Juegos/listar_usuarios.html', {'usuarios': usuarios})

@login_required
def ver_usuario(request, id):
    usuario = User.objects.get(id=id)
    return render(request, 'Biblioteca_Juegos/ver_usuario.html', {'usuario': usuario})

@login_required
def editar_usuario(request, id):
    usuario = User.objects.get(id=id)
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            if 'password' in form.cleaned_data and form.cleaned_data['password']:
                usuario.set_password(form.cleaned_data['password'])
            usuario.save()
            return redirect('listar_usuarios')
    else:
        form = RegistroUsuarioForm(instance=usuario)
    return render(request, 'Biblioteca_Juegos/registro.html', {'form': form})

@login_required
def borrar_usuario(request, id):
    usuario = User.objects.get(id=id)
    if request.user != usuario:  # Evita que uno se borre a sí mismo
        usuario.delete()
    return redirect('listar_usuarios')

