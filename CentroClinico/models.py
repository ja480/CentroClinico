from django.db import models
from django_google_maps import fields as map_fields

class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

# Create your models here.
# class Doctor(models.Model):
# 	name = models.CharField(max_length=50)
# 	email = models.EmailField(unique=True)
# 	gender = models.CharField(max_length=10)
# 	phonenumber = models.CharField(max_length=10)
# 	address = models.CharField(max_length=100)
# 	birthdate = models.DateField()
# 	bloodgroup = models.CharField(max_length=5)
# 	specialization = models.CharField(max_length=50)

# 	def __str__(self):
# 		return self.name


class Patient(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=16)
	gender = models.CharField(max_length=10)
	phonenumber = models.CharField(max_length=10)
	address = models.CharField(max_length=100)
	birthdate = models.DateField()
	bloodgroup = models.CharField(max_length=5)

	def __str__(self):
		return self.name

class Appointment(models.Model):
	doctorname = models.CharField(max_length=50)
	patientemail = models.EmailField(max_length=50)
	appointmentdate = models.DateField(max_length=10)
	appointmenttime = models.TimeField(max_length=10)
	symptoms = models.CharField(max_length=100)
	patientname = models.ForeignKey(Patient, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.patientname+" you have appointment with "+self.doctorname