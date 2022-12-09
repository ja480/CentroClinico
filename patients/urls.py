from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('register/', views.patient_register, name='patient_register'),
    path('update/', views.patient_update, name='patient_update'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/create/', views.appointment_register, name='appointment_create'),
    path('appointments/update/<int:pk>/', views.appointment_update, name='appointment_update'),
    path('appointments/delete/<int:pk>/', views.appointment_delete, name='appointment_delete'),
]