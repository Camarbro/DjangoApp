from django.contrib import admin
from .models import Doctor, Paciente ,Consultorio, Especialidad

# Register your models here.
@admin.register(Doctor)
class Doctor_admin(admin.ModelAdmin):
	list_display = ('doctor_id','doctor_name','get_speciality', 'get_consultorio','doctor_shift', 'get_patient')


@admin.register(Paciente)
class Paciente_admin(admin.ModelAdmin):
    list_display = ('paciente_id','paciente_name','paciente_age')

    #def get_doctor(self, obj):
        #return "\n".join([p.doctor_name for p in obj.Doctor.all()])

@admin.register(Consultorio)
class Consultorio_admin(admin.ModelAdmin):
	list_display = ('consultorio_name','consultorio_number')

@admin.register(Especialidad)
class Especialidad_admin(admin.ModelAdmin):
    list_display = ('speciality', 'speciality_branch')
