from django.conf.urls import url, include
from .views import home

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^Hospital/', include('Hospital.urls'), name = "Hospital_view"),
    url(r'^ParraCity/', include('ParraCity.urls'), name = 'ParraCity_view'),
    url(r'^ParraINC/', include('ParraINC.urls'), name = 'ParraINC')
]
