from django.urls import path
from . import views
from .views import JuegoListView

urlpatterns = [
    path('', views.home, name='home'),
    path('administrar/', views.administrar, name='administrar'),
    path('agregar/nvojuego', views.agregar_juegos, name='agregar_juegos'),
    path('acerca/', views.acerca, name='acerca'),
    path('buscar/', views.buscar_juego, name='buscar_juego'),
    path('listar/', views.listar_juegos, name='listar_juegos'),
    path('ver/<int:id>/', views.ver_juego, name='ver_juego'),
    path('editar/<int:id>/', views.editar_juego, name='editar_juego'),
    path('borrar/<int:id>/', views.borrar_juego, name='borrar_juego'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/ver/<int:id>/', views.ver_usuario, name='ver_usuario'),
    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/borrar/<int:id>/', views.borrar_usuario, name='borrar_usuario'),
    path('listar/', JuegoListView.as_view(), name='listar_juegos'),
]