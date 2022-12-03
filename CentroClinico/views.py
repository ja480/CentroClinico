from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,logout,login
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from citas.models import Appointment

def index(request):
	return render(request, 'Index.html')

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

# def login(request):
# 	error=""
# 	if request.method == 'POST':
# 		email = request.POST['email']
# 		password = request.POST['password']
# 		try:
# 			if password == password:
# 				return render(request,'index.html')
# 		except Exception as e:
# 			error = "yes"
# 	return render(request, 'login.html')


# def login(request):
#     error = ""
#     if request.method == 'POST':
#         u = request.POST['email']
#         p = request.POST['password']
#         user = authenticate(username=u, password=p)
#         try:
#             if user.is_staff:
#                 login(request, user)
#                 error = "no"
#             else:
#                 error = "yes"
#         except:
#             error = "yes"
#     return render(request,'registration/login.html', locals())


def login(request):
	error = ""

	if request.method == 'POST':
		u = request.POST.get['email']
		p = request.POST.get['password']
		user = authenticate(request,username=u,password=p)
		try:
			if user is not None:
				login(request,user)
				error = "no"
			return render (request,'index.html')	
		except Exception as e:
			error = "yes"
			#print(e)
			#raise e
	return render(request,'registration/login.html')

def Logout(request):
    logout(request)
    return redirect('index')
	