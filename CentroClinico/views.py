from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User,Group



def Index(request):
    return render(request, 'Index.html')

def RegCita(request):
    return render(request, 'RegCita.html')

def SobreNosotros(request):
    return render(request, 'SobreNosotros.html')

def Servicios(request):
    return render(request, 'Servicios.html')

# MOD

def CrearCuenta(request):
	error = ""
	user="none"
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		password = request.POST['password']
		repeatpassword = request.POST['repeatpassword']
		gender = request.POST['gender']
		phonenumber = request.POST['phonenumber']
		address = request.POST['address']
		birthdate = request.POST['dateofbirth']
		bloodgroup = request.POST['bloodgroup']
		try:
			if password == repeatpassword:
				Patient.objects.create(name=name,email=email,password=password,gender=gender,phonenumber=phonenumber,address=address,birthdate=birthdate,bloodgroup=bloodgroup)
				user = User.objects.create_user(first_name=name,email=email,password=password,username=email)
				pat_group = Group.objects.get(name='Patient')
				pat_group.user_set.add(user)
				#print(pat_group)
				user.save()
				#print(user)
				error = "no"
			else:
				error = "yes"
		except Exception as e:
			error = "yes"
			#print("Error:",e)
	d = {'error' : error}
	#print(error)
	return render(request,'crearcuenta.html',d)
	#return render(request,'createaccount.html')

def iniciarsesion(request):
	error=""
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		try:
			if password == password:
				return render(request,'Index.html')
		except Exception as e:
			error = "yes"
	return render(request, 'IniciarSesion.html')