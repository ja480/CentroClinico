from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Nos sirve para redireccionar despues de una accion, reveritendo
# Patrones de expresiones regulares
from django.urls import reverse
#Habilitamos el uso de mensaje de Django
from django.contrib import messages
#habilitamos los mensajes para class.based views
from django.contrib.messages.views import SuccessMessageMixin
#Habilitamos los formularios de django
from django import forms
from .models import Appointment
# Create your views here.

class ListadoCita(ListView):
    model = Appointment

class DetallesCita(DetailView):
    model = Appointment

class CrearCita(SuccessMessageMixin, CreateView):
    model = Appointment
    form = Appointment
    fields = '__all__'
    success_message = "Cita creada correctamente"
    def get_success_url(self):
        return reverse ('leer')

class CitasEliminar(SuccessMessageMixin, DeleteView):
    model = Appointment
    form = Appointment
    fields = '__all__'
    def get_success_url(self):
        sucess_message = "Registro eliminado correctamente"
        #messages.sucess(self.request, (sucess_message))
        return reverse ('leer')

class CitasActualizar(SuccessMessageMixin, UpdateView):
    model = Appointment
    form = Appointment
    fields = '__all__'
    success_message = "Vehiculo actualizado correctamente"
    def get_success_url(self):
        return reverse('leer')