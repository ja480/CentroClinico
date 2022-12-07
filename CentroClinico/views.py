from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,logout,login
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from citas.models import Appointment
# from .forms import FormAppointment


def index(request):
	return render(request, 'index.html')

def indexadmin(request):
	return render(request, 'indexadmin.html')

def regcita(request):
	return render(request, 'regcita.html')

def sobrenosotros(request):
	return render(request, 'sobrenosotros.html')

def servicios(request):
	return render(request, 'servicios.html')

# MOD

def crearcuenta(request):
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
				user.groups.add(pat_group)
				user.save()
				error = "no"
				
			else:
				error = "yes"
		except Exception as e:
			error = "yes"
	d = {'error' : error}
	return render(request,'crearcuenta.html',d)

# def login(request):
# 	error = ""

# 	if request.method == 'POST':
# 		u = request.POST.get['email']
# 		p = request.POST.get['password']
# 		user = authenticate(request,username=u,password=p)
# 		try:
# 			if user is not None:
# 				login(request,user)
# 				error = "no"
# 			return render (request,'index.html')	
# 		except Exception as e:
# 			error = "yes"

# 	return render(request,'registration/login.html')
def Login_admin(request):
	error = ""
	if request.method == 'POST':
		u = request.POST['username']
		p = request.POST['password']
		user = authenticate(username=u,password=p)
		try:
			if user.is_staff:
				login(request,user)
				error = "no"
			else:
				error = "yes"
		except:
			error = "yes"
	d = {'error' : error}
	return render(request,'registration/adminlogin.html',d)

def loginpage(request):
	error = ""
	page = ""
	if request.method == 'POST':
		u = request.POST['email']
		p = request.POST['password']
		user = authenticate(request,username=u,password=p)
		try:
			if user is not None:
				login(request,user)
				error = "no"
				g = request.user.groups.all()[0].name
				if g == 'Doctor':
					page = "doctor"
					return render(request,'index.html')
				elif g == 'Patient':
					page = "patient"
					return render(request,'index.html')
			else:
				error = "yes"
		except:
			error = "yes"
	d = {'error' : error}
	return render(request,'registration/login.html',d)

def Logout(request):
	logout(request)
	return redirect('index')

def Logout_admin(request):
	if not request.user.is_staff:
		return redirect('login_admin')
	logout(request)
	return redirect('login_admin')
	
# def regcita(request):
# 	form = FormAppointment(request.POST or None)

# 	if request.method == "POST":
# 		if form.is_valid():
# 			form.save()
# 		return redirect ('index')
# 	context = {
# 		"form":form
# 	}
# 	return render(request, 'regcita.html', context)

def MakeAppointments(request):
	error = ""
	if not request.user.is_active:
		return redirect('loginpage')
	alldoctors = Doctor.objects.all()
	d = { 'alldoctors' : alldoctors }	
	if request.user.groups.filter(name='Patient').exists():
		if request.method == 'POST':
			print('ok')
			doctoremail = request.POST['doctoremail']
			doctorname = request.POST['doctorname']
			patientname = request.POST['patientname']
			patientemail = request.POST['patientemail']
			appointmentdate = request.POST['appointmentdate']
			appointmenttime = request.POST['appointmenttime']
			symptoms = request.POST['symptoms']
			try:
				Appointment.objects.create(doctorname=doctorname,doctoremail=doctoremail,patientname=patientname,patientemail=patientemail,appointmentdate=appointmentdate,appointmenttime=appointmenttime,symptoms=symptoms,status=True,prescription="")
				error = "no"
			except:
				error = "yes"
			e = {"error":error}
			return render(request,'regcita.html',e)
		elif request.method == 'GET':
			return render(request,'regcita.html',d)
	return render(request,'regcita.html')