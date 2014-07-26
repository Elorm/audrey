from django.conf.urls import patterns, url
from bridal import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^home/$', views.home, name='home'),
	url(r'^about/$', views.about, name='about'),
	url(r'^gallery/$', views.gallery, name='gallery'),
	url(r'^contact/$', views.contact, name='contact'),	
)
