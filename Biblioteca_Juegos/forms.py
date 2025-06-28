from django import forms
from .models import JuegoNvo
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import UsuarioLogin

class JuegoNvoForm(forms.ModelForm):
    class Meta:
        model = JuegoNvo
        fields = '__all__'

class BusquedaForm(forms.Form):
    nombre = forms.CharField(label='Buscar por nombre', max_length=100)


class UserLoginForm(AuthenticationForm):
    pass

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = UsuarioLogin
        fields = ['username', 'email', 'avatar']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('password2'):
            self.add_error('password2', 'Las contraseñas no coinciden.')
        return cleaned_data