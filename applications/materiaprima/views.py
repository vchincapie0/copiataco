from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,DetailView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render

#Importacion modelos y formularios
from .models import MateriaPrima,Desinfeccion,CaracteristicasOrganolepticas, Existenciamp
from .forms import MateriaPrimaForm,CaracteristicasMPForm,CaracteristicasMPUpdateForm,DesinfeccionMPForm, DesinfeccionMPUpdateForm


# Create your views here.

class MateriaPrimaListView(LoginRequiredMixin, ListView):
    '''Clase para mostrar los datos de las materias primas'''
    model = MateriaPrima
    template_name = "materiaprima/lista_mp.html"
    login_url=reverse_lazy('users_app:login')
    paginate_by=10
    context_object_name = 'materiaprima'

    def get_queryset(self):
        '''Funcion que toma de la barra de busqueda la pablabra clave para filtrar'''
        palabra_clave= self.request.GET.get("kword",'')
        lista = MateriaPrima.objects.filter(
            mp_nombre__icontains = palabra_clave
        ).prefetch_related('caracteristicasorganolepticas_set')
        return lista

class MateriaPrimaCreateView(LoginRequiredMixin, CreateView):
    '''Clase donde se crea una nueva materia prima'''
    model = MateriaPrima
    template_name = "materiaprima/add_mp.html"
    login_url=reverse_lazy('users_app:login')
    #Campos que se van a mostrar en el formulario
    form_class = MateriaPrimaForm
    #url donde se redirecciona una vez acaba el proceso el "." es para redireccionar a la misma pagina
    success_url= reverse_lazy('mp_app:lista_mp') 

class CaracteristicasMateriaPrimaCreateView(LoginRequiredMixin, CreateView):
    '''Vista para la creacion de las caracteristicas organolepticas de la materia prima'''
    model = CaracteristicasOrganolepticas
    template_name = "materiaprima/caracteristicas_mp.html"
    login_url=reverse_lazy('users_app:login')
    #Campos que se van a mostrar en el formulario
    form_class = CaracteristicasMPForm
    #url donde se redirecciona una vez acaba el proceso el "." es para redireccionar a la misma pagina
    success_url= reverse_lazy('mp_app:lista_mp')
    
class CaracteristicasMateriaPrimaUpdateView(LoginRequiredMixin, UpdateView):
    '''Vista para la edicion de las caracteristicas organolepticas de la materia prima'''
    model = CaracteristicasOrganolepticas
    template_name = "materiaprima/updateCaracteristicas_mp.html"
    login_url=reverse_lazy('users_app:login')
    #Campos que se van a mostrar en el formulario
    form_class = CaracteristicasMPUpdateForm
    #url donde se redirecciona una vez acaba el proceso el "." es para redireccionar a la misma pagina
    success_url= reverse_lazy('mp_app:lista_mp')
    
class DesinfeccionMateriaPrimaCreateView(LoginRequiredMixin, CreateView):
    '''Vists para la creacion de la desinfeccion de la materia prima'''
    model = Desinfeccion
    template_name = "materiaprima/desinfeccion_mp.html"
    login_url=reverse_lazy('users_app:login')
    #Campos que se van a mostrar en el formulario
    form_class = DesinfeccionMPForm
    #url donde se redirecciona una vez acaba el proceso el "." es para redireccionar a la misma pagina
    success_url= reverse_lazy('mp_app:lista_mp')

    def get_queryset(self):
        pk = self.kwargs['mp_lote']
        lista = MateriaPrima.objects.filter(
            desinfeccion__mp_lote = pk
        )
        return lista
    
    # Example view handling the form submission
    def desinfeccion_form_view(request):
        if request.method == 'POST':
            form = DesinfeccionMPForm(request.POST)
        if form.is_valid():
            # Create a new instance of Desinfeccion
            desinfeccion_instance = form.save(commit=False)
            # Set the current logged-in user as the responsable
            desinfeccion_instance.responsable = request.user
            # Save the instance
            desinfeccion_instance.save()
            # Redirect or do whatever you need after successful form submission
            return reverse_lazy('mp_app:lista_mp')
        else:
            form = DesinfeccionMPForm()
        return render(request, 'materiaprima/desinfeccion_mp.html', {'form': form})

class DesinfeccionMateriaPrimaUpdateView(LoginRequiredMixin, UpdateView):
    '''Vista para la edición de la desinfeccion de la materia prima'''
    model = Desinfeccion
    template_name = "materiaprima/updateDesinfeccion_mp.html"
    login_url=reverse_lazy('users_app:login')
    #Campos que se van a mostrar en el formulario
    form_class = DesinfeccionMPUpdateForm
    #url donde se redirecciona una vez acaba el proceso el "." es para redireccionar a la misma pagina
    success_url= reverse_lazy('mp_app:lista_mp')
    
class MateriaPrimaDetailView(LoginRequiredMixin, DetailView):
    '''Vista donde se muestran los detalles de la materia prima'''
    model = MateriaPrima
    template_name = "materiaprima/detail_mp.html"
    login_url=reverse_lazy('users_app:login')
    context_object_name = 'materiaprima'

class ExistenciampView(LoginRequiredMixin, ListView):
    '''Vists para la creacion de la existencias materia prima'''
    model = Existenciamp
    template_name = "materiaprima/existencia_mp.html"
    login_url=reverse_lazy('users_app:login')
    success_url= reverse_lazy('mp_app:exitencia_mp')

