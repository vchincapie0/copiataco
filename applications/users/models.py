from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import UserManager
# Create your models here.

class User(AbstractUser, PermissionsMixin):
    '''Clase para crear usuarios en bd'''

    ROL_CHOICES = (
        ('1','Administrador'),
        ('2','Operario'),
    )

    username = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    rol=models.CharField(max_length=1,choices=ROL_CHOICES)
    #
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD='username'

    REQUIRED_FIELDS=['name','last_name']

    objects = UserManager()

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.nombres+'-'+self.apellidos


