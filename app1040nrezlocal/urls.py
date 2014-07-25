from django.conf.urls import patterns, url
from app1040nrezlocal import views

urlpatterns = patterns('',
        url(r'^$', views.index), # index.html
		url(r'^output/$', views.outputPdf),
		url(r'^styled/$', views.styled),
		url(r'^postTax/$', views.postTax),
		)