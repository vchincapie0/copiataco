from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from . models import User

class UserRegisterForm(forms.ModelForm):
    """Form definition for UserRegister."""

    password=forms.CharField(
        label='Contraseña:',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder':'Contraseña'}
        ),
    )

    password2=forms.CharField(
        label='Repetir contraseña:',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder':'Contraseña'}
        )
    )

    class Meta:
        """Meta definition for UserRegisterform."""

        model = User
        fields = ('username',
                  'name',
                  'last_name',
                  'rol',)
        
    def clean_username(self):
        '''Función para validar si el usuario ya existe'''
        username = self.cleaned_data.get('username')

        # Verificar si ya existe un usuario con el mismo nombre de usuario
        if User.objects.filter(username=username).exists():
            raise ValidationError('Este nombre de usuario ya está en uso. Elige otro.')

        return username
        

    def clean_password(self):
        '''Funcion para validar que las contraseñas tenga > 6 caracteres'''
        contraseña = self.cleaned_data.get('password')

        if len(contraseña) <= 5:
            self.add_error('password','La contraseña debe tener más de 5 caracteres.')
        
        return contraseña

    def clean_password2(self):
        '''Funcion para validar que las contraseñas coincidan'''
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            self.add_error('password2','Las contraseñas no coinciden.')

    def clean_name(self):
        '''Función para validar el campo de nombre'''
        name = self.cleaned_data.get('name')

        if any(char.isdigit() or not char.isalpha() for char in name):
            raise ValidationError('El nombre solo puede contener letras.')

        return name
    
    def clean_last_name(self):
        '''Función para validar el campo de apellido'''
        last_name = self.cleaned_data.get('last_name')

        if any(char.isdigit() or not char.isalpha() for char in last_name):
            raise ValidationError('El apellido solo puede contener letras.')

        return last_name
    
class UserUpdateForm(forms.ModelForm):
    '''Clase de formulario para editar un usuario'''
    password=forms.CharField(
            label='Contraseña:',
            required=True,
            widget=forms.PasswordInput(
                attrs={'placeholder':'Contraseña Nueva'}
            )
        )    

    password2=forms.CharField(
        label='Repetir contraseña:',
            required=True,
            widget=forms.PasswordInput(
                attrs={'placeholder':'Repetir Contraseña Nueva'}
            )
        ) 

    class Meta:
        model = User
        fields = ['username', 'name', 'last_name', 'rol']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        # Deshabilitar el campo de username
        self.fields['username'].disabled = True

    def clean_name(self):
        '''Función para validar el campo de nombre'''
        name = self.cleaned_data.get('name')

        if any(char.isdigit() or not char.isalpha() for char in name):
            raise ValidationError('El nombre solo puede contener letras.')

        return name
    
    def clean_last_name(self):
        '''Función para validar el campo de apellido'''
        last_name = self.cleaned_data.get('last_name')

        if any(char.isdigit() or not char.isalpha() for char in last_name):
            raise ValidationError('El apellido solo puede contener letras.')

        return last_name
    
    def clean_password(self):
        '''Funcion para validar que las contraseñas tenga > 6 caracteres'''
        contraseña = self.cleaned_data.get('password')

        if len(contraseña) <= 5:
            self.add_error('password','La contraseña debe tener más de 5 caracteres.')
        
        return contraseña

    def clean_password2(self):
        '''Funcion para validar que las contraseñas coincidan'''
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            self.add_error('password2','Las contraseñas no coinciden.')
    