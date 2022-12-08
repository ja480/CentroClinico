from django.contrib import admin

from doctors.models import *

class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['name']
    
class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
    ]
    
class DiaryAdmin(admin.ModelAdmin):
    list_display = [
        'day', 'doctor', 'schedule'
    ]
    
admin.site.register(Speciality, SpecialityAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Diary, DiaryAdmin)