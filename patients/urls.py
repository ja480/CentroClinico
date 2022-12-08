from django.urls import path
from . import views

app_name = 'patients'

urlpatterns = [
    path('register/', views.patient_register, name='patient_register'),
    path('update/', views.patient_update, name='patient_update'),
    path('consults/', views.consult_list, name='consult_list'),
    path('consults/create/', views.consult_register, name='consult_create'),
    path('consults/update/<int:pk>/', views.consult_update, name='consult_update'),
    path('consults/delete/<int:pk>/', views.consult_delete, name='consult_delete'),
]