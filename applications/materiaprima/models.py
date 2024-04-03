from django.db import models
from applications.users.models import User
from django.contrib.auth import get_user_model

# Create your models here.

  
class MateriaPrima(models.Model):

    TIPO_CHOICES=(
        ('0','Proteina'),
        ('1','Lácteo'),
        ('2','Verduras'),
        ('3','Frutas'),
    )

    mp_lote = models.IntegerField('Lote', primary_key=True)
    mp_nombre = models.CharField('Nombre',max_length=50)
    mp_tipo=models.CharField('Tipo',max_length=1,choices=TIPO_CHOICES,default=0)
    mp_cantidad=models.IntegerField(default=100)
    mp_fechallegada=models.DateField('Fecha Ingreso')
    mp_fechavencimiento = models.DateField('Fecha Vencimiento')

    def __str__(self):
        return str(self.mp_lote)+'-'+self.mp_nombre

class CaracteristicasOrganolepticas(models.Model):

    ESTADO_CHOICES=(
        ('0','Aprobado'),
        ('1','No Aprobado'),
    )

    mp_lote=models.ForeignKey(MateriaPrima,on_delete=models.CASCADE)
    olor = models.BooleanField('Olor',default=False)
    textura = models.BooleanField('Textura',default=False)
    limpieza = models.BooleanField('Limpieza',default=False)
    empaque = models.BooleanField('Empaque',default=False)
    color = models.BooleanField('Color',default=False)
    estado=models.CharField('Estado',max_length=1,choices=ESTADO_CHOICES)
    
    def __str__(self):
        return str(self.mp_lote)+'-'+self.estado
    
class Desinfeccion(models.Model):
    mp_lote=models.ForeignKey(MateriaPrima,on_delete=models.CASCADE)
    des_nombre=models.CharField('Nombre del Desinfectante',max_length=20)
    concentracion = models.IntegerField('Concentración')
    responsable = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tiempo_inicio=models.TimeField('Tiempo de Inicio')
    tiempo_fin=models.TimeField('Fin Desinfección')
    obsevacion=models.CharField('Observaciones',max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.mp_lote)+'-'+self.des_nombre
    
    def save(self, *args, **kwargs):
        # Check if responsable is empty
        if not self.responsable:
            # Get the currently logged-in user
            user = get_user_model().objects.first()  # Or use the appropriate logic to get the logged-in user
            if user:
                self.responsable = user
        super().save(*args, **kwargs)

    
    
class Existenciamp(models.Model):
    exiMP_codigo=models.PositiveIntegerField('codigo', primary_key=True)
    mp_lote=models.ForeignKey(MateriaPrima,on_delete=models.CASCADE)
    exiMP_cantidadIngresada=models.PositiveBigIntegerField('cantidad ingresada')
    exiMP_cantidadEgresada=models.PositiveBigIntegerField('cantidad de salida')

    def __str__(self):
        return str(self.mp_lote)+'-'+self.exiMP_cantidadIngresada+self.exiMP_cantidadEgresada

    
