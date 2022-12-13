from datetime import date
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models.fields.related import ForeignKey, OneToOneField
import logging

class Consultingroom(models.Model):
    name = models.CharField(verbose_name="Name", max_length=200)
        
    def __str__(self):
        return f'{self.name}'
    
class Doctor(models.Model):
    name = models.CharField(verbose_name="Name", max_length=200)
    email = models.EmailField(verbose_name="Email")
    speciality = models.CharField(verbose_name="Speciality", max_length=200)
    consultingroom = ForeignKey(Consultingroom,on_delete=models.CASCADE,related_name='doctors')
    
    def __str__(self):
        return f'{self.name}'

def validate_day(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('No es posible escoger un dia atrasado.')
    if (weekday == 5) or (weekday == 6):
        raise ValidationError('Seleccione un dia habil de la semana.')

class Diary(models.Model):
    doctor = ForeignKey(Doctor, on_delete=models.CASCADE, related_name='diary')
    day = models.DateField(help_text="Ingrese una fecha", validators=[validate_day])
    
    schedules = (
        ("1", "07:00 a 08:00"),
        ("2", "08:00 a 09:00"),
        ("3", "09:00 a 10:00"),
        ("4", "10:00 a 11:00"),
        ("5", "11:00 a 12:00"),
    )
    schedule = models.CharField(max_length=10, choices=schedules)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuario', 
        on_delete=models.CASCADE
    )
    class Meta:
        unique_together = ['schedule', 'day']
        
    def __str__(self):
        return f'{self.day.strftime("%b %d %Y")} - {self.get_schedule_display()} - {self.doctor}'