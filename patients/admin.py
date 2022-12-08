from django.contrib import admin
from .models import Patient, Consult

class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'genero',
    ]
    
class ConsultAdmin(admin.ModelAdmin):
    list_display = [
        'diary', 'patient',
    ]
    
admin.site.register(Patient, PatientAdmin)
admin.site.register(Consult, ConsultAdmin)