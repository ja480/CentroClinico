from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render


def inicio(request):

    ahora=datetime.datetime.now()
    doc_externo=loader.get_template('plantilla.html')
    return render(request, "plantilla.html",{"hoy":ahora})

def clinica(request):
    return render(request,'clinica.html')

def contacto(request):
    return render(request,'contacto.html')
        
def servicios(request):
    return render(request,'servicios.html')

def acerca(request):
    return render(request,'acerca_de.html')

def agenda(request):
    return render(request,'agendar_cita.html')

def especialidades(request):
    return render(request,'especialidades.html')

def examenes(request):
    return render(request,'examenes.html')
