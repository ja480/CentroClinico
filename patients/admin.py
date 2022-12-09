from django.contrib import admin
from .models import Patient, Appointment

class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'genero',
    ]
    
class AppointmentAdmin(admin.ModelAdmin):
    list_display = [
        'diary', 'patient',
    ]
    
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)