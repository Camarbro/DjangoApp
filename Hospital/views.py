from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from .models import Doctor, Paciente, Consultorio, Especialidad
from django.views.generic import CreateView, ListView

# Create your views here.
class  Register_Doctor(CreateView):
    template_name = 'Hospital/Register_Doctor.html'
    model = Doctor
    fields = '__all__'
    success_url = reverse_lazy('home_view')


class Register_Patient(CreateView):
    template_name = 'Hospital/Register_Patient.html'
    model = Paciente
    fields = '__all__'
    success_url = reverse_lazy('home_view')

class Register_Consultory(CreateView):
    template_name = 'Hospital/Register_Consultory.html'
    model = Consultorio
    fields = '__all__'
    success_url = reverse_lazy('home_view')

class Register_Speciality(CreateView):
        template_name = 'Hospital/Register_Speciality.html'
        model = Especialidad
        fields = '__all__'
        success_url = reverse_lazy('home_view')

class Report_Doctor(ListView):
    template_name = 'Hospital/Report_Doctor.html'
    model = Doctor

class Report_DoctorPatient(ListView):
    template_name = 'Hospital/Report_DoctorPatient.html'
    model = Doctor

class Report_DoctorConsultory(ListView):
    template_name = 'Hospital/Report_DoctorConsultory.html'
    model = Doctor


class Report_Patient(ListView):
    template_name = 'Hospital/Report_Patient.html'
    model = Paciente



def home(request):
    return render(request, 'Hospital/home.html')
