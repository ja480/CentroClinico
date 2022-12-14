from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    path('register/doctor/', views.doctor_register, name='doctor_register'),
    path('register/speciality/', views.consultingroom_register, name='consultingroom_register'),
    path('scheduling/', views.diary_register, name='scheduling_appointment'),
    path('scheduling/update/<int:pk>/', views.diary_update, name='scheduling_appointment_update'),
    path('scheduling/delete/<int:pk>/', views.diary_delete, name='scheduling_appointment_delete'),
    path('mine/consults/', views.diary_list, name="diary_list"),
    path('admin/list/doctors/', views.doctor_list, name="doctor_list"),
    path('admin/list/consultingroom/', views.consultingroom_list, name="consultingroom_list")
    
]