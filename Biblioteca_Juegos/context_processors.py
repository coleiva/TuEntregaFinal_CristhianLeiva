from .models import UsuarioLogin

def avatar_context(request):
    if request.user.is_authenticated:
        return {'avatar_usuario': request.user.avatar}
    return {'avatar_usuario': None}