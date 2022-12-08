from django.conf import settings
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.db import models
from doctors.models import Diary 

class Patient(models.Model):
    GENERO = (
        ("MAS", "Masculino"),
        ("FEM", "Femenino")
    )
    
    genero = models.CharField(max_length=9, choices=GENERO,)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuario', 
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f'{self.user.name}'
    
class Consult(models.Model):
    diary =  OneToOneField(Diary, on_delete=models.CASCADE, related_name='consult')
    patient = ForeignKey(Patient, on_delete=models.CASCADE, related_name='consult')
    
    class Meta:
        unique_together = ('diary', 'patient')
        
    def __str__(self):
        return f'{self.diary} - {self.patient}'