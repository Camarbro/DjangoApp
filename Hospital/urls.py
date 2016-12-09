from django.conf.urls import url,  include
from .views import home, Report_DoctorConsultory, Register_Doctor, Report_Doctor, Report_Patient, Register_Doctor, Register_Patient, Register_Speciality, Register_Consultory, Report_DoctorPatient

urlpatterns = [

    url(r'^$', home, name="home_view"),
    url(r'^Report_Doctor/$', Report_Doctor.as_view(), name = 'Report_Doctor_View'),
    url(r'^Report_Patient/$', Report_Patient.as_view(), name= 'Report_Patient_view'),
    url(r'^Register_Doctor/$', Register_Doctor.as_view(), name = 'Register_Doctor_view'),
    url(r'^Register_Patient/$', Register_Patient.as_view(), name='Register_Patient_view'),
    url(r'^Register_Speciality/$', Register_Speciality.as_view(), name='Register_Speciality_view'),
    url(r'^Register_Consultory/$', Register_Consultory.as_view(), name='Register_Consultory_view'),
    url(r'^Report_DoctorPatient/$', Report_DoctorPatient.as_view(), name= 'Report_DoctorPatient_view'),
    url(r'^Report_DoctorConsultory/$', Report_DoctorConsultory.as_view(), name= 'Report_DoctorConsultory_view'),
]
