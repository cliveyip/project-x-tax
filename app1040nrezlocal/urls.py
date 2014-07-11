from django.conf.urls import patterns, url
from app1040nrezlocal import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
		url(r'^output/$', views.outputPdf, name='output pdf'), # NEW MAPPING!
		url(r'^styled/$', views.styled, name='styled'), # NEW MAPPING!
		)