#Importación de Librerias
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import  redirect
from django.views.generic import View,ListView,UpdateView, FormView, DeleteView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy,reverse

#Importacion modelos y formularios
from .models import User
from .forms import UserRegisterForm, UserUpdateForm 

# Create your views here.

class UsersListView(LoginRequiredMixin, ListView):
    '''vista que muestra todos los usuarios registrados'''
    model = User
    template_name = "usuarios/list_user.html"
    login_url=reverse_lazy('users_app:login')
    paginate_by=5
    context_object_name='usuarios'

    def get_queryset(self):
        palabra_clave= self.request.GET.get("kword",'')
        lista = User.objects.filter(
            name__icontains = palabra_clave
        )
        return lista

class UserRegisterView(LoginRequiredMixin,FormView):
    '''Vista que registra usuarios del modelo user'''
    template_name ='usuarios/add_user.html'
    login_url=reverse_lazy('users_app:login')
    form_class=UserRegisterForm
    success_url=reverse_lazy('users_app:list_user')

    def form_valid(self, form):
        '''Funcion para guardar los datos de user'''
        User.objects.create_user(
            form.cleaned_data['name'],
            form.cleaned_data['last_name'],
            form.cleaned_data['username'],
            form.cleaned_data['password'],
            rol=form.cleaned_data['rol'],

        )
        return super(UserRegisterView, self).form_valid(form)

class UserRegisterView2(FormView):
    '''Vista que registra usuarios del modelo user'''
    template_name ='usuarios/register_user.html'
    form_class=UserRegisterForm
    success_url=reverse_lazy('users_app:login')

    def form_valid(self, form):
        '''Funcion para guardar los datos de user'''
        User.objects.create_user(
            form.cleaned_data['name'],
            form.cleaned_data['last_name'],
            form.cleaned_data['username'],
            form.cleaned_data['password'],
            rol=form.cleaned_data['rol'],

        )
        return super(UserRegisterView2, self).form_valid(form)    
    
class UserUpdateView(LoginRequiredMixin, UpdateView):
    '''Vista para actualizar los datos de user'''
    model = User
    template_name = "usuarios/update_user.html"
    login_url=reverse_lazy('users_app:login')
    form_class=UserUpdateForm
    success_url= reverse_lazy('users_app:list_user')

class UserDeleteView(LoginRequiredMixin, DeleteView):
    '''Vista para borrar user'''
    model = User
    template_name = "usuarios/delete_user.html"
    login_url=reverse_lazy('users_app:login')
    success_url= reverse_lazy('users_app:list_user')

class LogIn(LoginView):
    '''Vista para login'''
    template_name = 'usuarios/login.html'
    success_url = reverse_lazy('home_app:home')

    def form_valid(self, form):
        # Recoge los datos del formulario
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # Autentica al usuario utilizando el sistema de autenticación de Django
        user = authenticate(username=username, password=password)

        if user is not None:
            # Inicia sesión para el usuario autenticado
            login(self.request, user)
            return redirect(self.get_success_url())

class LogOut(View):
    '''Vista para cerrar sesion'''
    def get(self,request,*args,**kwargs):
        logout(request)

        return HttpResponseRedirect(
            reverse('users_app:login')
        )
    
