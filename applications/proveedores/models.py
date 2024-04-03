from django.db import models

# Create your models here.

class Proveedores(models.Model):
    '''Clase para la creacion de tabla proveedores en bd'''
    prov_id=models.AutoField('id',primary_key=True)
    nit = models.IntegerField('NIT',unique=True)
    prov_nombre=models.CharField('Nombre',max_length=40)
    prov_telefono=models.CharField('Telefono',max_length=10)

    def __str__(self):
        return f"{self.nit}-{self.prov_nombre}"
