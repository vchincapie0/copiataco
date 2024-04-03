from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import CaracteristicasOrganolepticas, Desinfeccion

@receiver(pre_save, sender=CaracteristicasOrganolepticas)
def actualizar_estado(sender, instance, **kwargs):
    # Verificar si todas las características son iguales a cero
    if instance.olor == instance.textura == instance.limpieza == instance.empaque == instance.color == True:
        # Establecer el estado como 'Aprobado'
        instance.estado = '0'  # Suponiendo que '0' corresponde a 'Aprobado' según tus opciones
    else:
        instance.estado = '1'

# Signal receiver function to automatically set the responsable field after saving Desinfeccion instance
@receiver(post_save, sender=Desinfeccion)
def set_responsable(sender, instance, created, **kwargs):
    if created and not instance.responsable:
        user = get_user_model().objects.first()  # Or use the appropriate logic to get the logged-in user
        if user:
            instance.responsable = user
            instance.save(update_fields=['responsable'])