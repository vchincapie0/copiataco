from django import forms
from django.utils import timezone
from .models import MateriaPrima, Desinfeccion, CaracteristicasOrganolepticas

class MateriaPrimaForm(forms.ModelForm):
    """Form definition for Materia Prima."""

    class Meta:
        """Meta definition for MateriaPrimaform."""

        model = MateriaPrima
        fields = (
            'mp_lote',
            'mp_nombre',
            'mp_tipo',
            'mp_cantidad',
            'mp_fechallegada',
            'mp_fechavencimiento',
            )
        
        widgets={
            'mp_nombre':forms.TextInput(attrs={'placeholder': 'Nombre Materia Prima'}),
            'mp_fechallegada':forms.SelectDateWidget(),
            'mp_fechavencimiento':forms.SelectDateWidget(),
        }
    
    def clean_mp_cantidad(self):
        cantidad = self.cleaned_data['mp_cantidad']
        if cantidad <= 0:
            raise forms.ValidationError("La cantidad debe ser un número mayor que 0.")
        return cantidad
    
    def clean_mp_fechallegada(self):
        fecha_llegada = self.cleaned_data['mp_fechallegada']
        fecha_actual = timezone.now().date()
        tres_dias_atras = fecha_actual - timezone.timedelta(days=3)

        # Comprueba si la fecha de llegada está dentro del rango permitido
        if fecha_llegada > fecha_actual or fecha_llegada < tres_dias_atras:
            raise forms.ValidationError('La fecha de llegada debe ser el día actual o hasta 3 días antes.')
        
        return fecha_llegada
    
    def clean_mp_fechavencimiento(self):
        fecha_vencimiento = self.cleaned_data['mp_fechavencimiento']
        fecha_actual = timezone.now().date()

        # Comprueba si la fecha de vencimiento es anterior a la fecha actual
        if fecha_vencimiento < fecha_actual:
            raise forms.ValidationError('La fecha de vencimiento debe ser posterior a la fecha actual.')

        return fecha_vencimiento

class CaracteristicasMPForm(forms.ModelForm):

    class Meta:

        model = CaracteristicasOrganolepticas
        fields=(
            'mp_lote',
            'olor',
            'textura',
            'limpieza',
            'empaque',
            'color',
             
        )

        widgets={
                'olor':forms.CheckboxInput(),
                'textura':forms.CheckboxInput(),
                'limpieza':forms.CheckboxInput(),
                'empaque':forms.CheckboxInput(),
                'color':forms.CheckboxInput(),    
            }
        
class CaracteristicasMPUpdateForm(forms.ModelForm):

    class Meta:

        model = CaracteristicasOrganolepticas
        fields=(
            'mp_lote',
            'olor',
            'textura',
            'limpieza',
            'empaque',
            'color',
             
        )

        widgets={
                'mp_lote':forms.TextInput(attrs={'readonly':'readonly'}),
                'olor':forms.CheckboxInput(),
                'textura':forms.CheckboxInput(),
                'limpieza':forms.CheckboxInput(),
                'empaque':forms.CheckboxInput(),
                'color':forms.CheckboxInput(),    
            }
                       
class DesinfeccionMPForm(forms.ModelForm):

    class Meta:

        model = Desinfeccion
        fields=(
            'mp_lote',
            'des_nombre',
            'concentracion',
            'tiempo_inicio',
            'tiempo_fin',
            'obsevacion', 
             
        )

        widgets={
            'des_nombre':forms.TextInput(attrs={'placeholder': 'Nombre Desinfectante'}),
            'concentracion':forms.NumberInput(attrs={'max_length': '2'}),
            'tiempo_inicio':forms.TimeInput(attrs={'type':'time'}),
            'tiempo_fin':forms.TimeInput(attrs={'type':'time'}),
            'obsevacion':forms.Textarea(attrs={'placeholder': 'Escriba su observacion'})    
            }    
        
class DesinfeccionMPUpdateForm(forms.ModelForm):

    class Meta:

        model = Desinfeccion
        fields=(
            'mp_lote',
            'des_nombre',
            'concentracion',
            'tiempo_inicio',
            'tiempo_fin',
            'obsevacion', 
             
        )

        widgets={
            'mp_lote':forms.TextInput(attrs={'readonly':'readonly'}),
            'des_nombre':forms.TextInput(attrs={'placeholder': 'Nombre Desinfectante'}),
            'concentracion':forms.NumberInput(attrs={'max_length': '2'}),
            'tiempo_inicio':forms.TimeInput(attrs={'type':'time'}),
            'tiempo_fin':forms.TimeInput(attrs={'type':'time'}),
            'obsevacion':forms.Textarea(attrs={'placeholder': 'Escriba su observacion'})    
            }    