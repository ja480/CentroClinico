from django.contrib import admin

from doctors.models import *
    
class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'speciality',
    ]
    
class DiaryAdmin(admin.ModelAdmin):
    list_display = [
        'day', 'doctor', 'schedule',
    ]
    
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Diary, DiaryAdmin)