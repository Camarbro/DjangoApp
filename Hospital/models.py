from django.db import models

# Create your models here.
class Consultorio(models.Model):
    consultorio_name = models.CharField(max_length=64)
    consultorio_number = models.IntegerField()

    def __unicode__(self):
        return self.consultorio_name

class Especialidad(models.Model):
    speciality = models.CharField(max_length=64)
    speciality_branch = models.CharField(max_length=64)

    def __unicode__(self):
        return 'Especialidad: %s ' %(self.speciality_branch)

class Paciente(models.Model):
    paciente_id = models.IntegerField()
    paciente_name = models.CharField(max_length = 64)
    paciente_age = models.IntegerField()

    def __unicode__(self):
        return 'Paciente ID: %d - Paciente Name: %s' %(self.paciente_id, self.paciente_name)


class Doctor(models.Model):
    doctor_id = models.IntegerField()
    doctor_name = models.CharField(max_length = 64)
    doctor_speciality = models.ManyToManyField(Especialidad)
    consultorio = models.ManyToManyField(Consultorio)
    Matutino = 'MAT'
    Vespertino = 'VES'
    Nocturno = 'NOC'
    HORARIOS = (
        (Matutino, 'Matutino'),
        (Vespertino, 'Vespertino'),
        (Nocturno, 'Nocturno'),
    )
    doctor_shift = models.CharField(max_length = 3, choices = HORARIOS, default = Matutino)
    Paciente = models.ManyToManyField(Paciente)


    def __unicode__(self):
        return 'Doctor ID: %d - Doctor Name: %s' %(self.doctor_id, self.doctor_name)

    def get_patient(self):
        return "\n".join([p.paciente_name for p in self.Paciente.all()])

    def get_speciality(self):
        return "\n".join([p.speciality_branch for p in self.doctor_speciality.all()])

    def get_consultorio(self):
        return "\n".join([p.consultorio_name for p in self.consultorio.all()])
