from django import forms
from .models import Appointment

class FormAppointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'doctorname', 'patientemail','patientemail',
            'appointmenttime','symptoms','patientname'
        ]    
