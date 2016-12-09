from django.conf.urls import url, include
from .views import home, Reports, quality, Order_detail, Order_new, Order_edit, Delete_Order, SignUp
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', home, name="home_view"),
    url(r'^reports/$', Reports.as_view(), name = 'reports_view'),
    url(r'^neworder/$', Order_new , name = 'Order_New_view' ),
    url(r'^quality/$', quality, name = 'quality_view'),
    url(r'^quality/(?P<pk>[0-9]+)/$', Order_detail, name = 'Order_detail_view'),
    url(r'^quality/(?P<pk>[0-9]+)/edit/$', Order_edit, name='Order_edit_view'),
    url(r'^quality/(?P<pk>[0-9]+)/delete/$', Delete_Order, name = 'delete_order_view'),
    url(r'^login/$', login , {'template_name': 'ParraINC/LogIn.html'}, name='login'),
	url(r'^logout/$', logout ,{'template_name': 'ParraINC/LogOut.html'}, name='logout'),
    url(r'^SignUp/$', SignUp.as_view(), name = 'SignUp')
]
