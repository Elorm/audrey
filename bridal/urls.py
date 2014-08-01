from django.conf.urls import patterns, url
from bridal import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^home/$', views.home, name='home'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contact/$', views.contact, name='contact'),
    url(r'^gallery/$', views.AlbumListView.as_view(), name='gallery'),
    url(r'^gallery/page/(?P<page>[0-9]+)/$', views.AlbumListView.as_view(), name='gallery_paginated'),
    url(r'^album/(?P<slug>[\.\w-]+)/$', views.AlbumDetailView.as_view(), name='bridal_album_detail'),	
    url(r'^album/(?P<slug>[\.\w-]+)/page/(?P<page>[0-9]+)/$', views.AlbumDetailView.as_view(), name='album_paginated'),
)
