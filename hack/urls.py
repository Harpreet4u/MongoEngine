from django.conf.urls import patterns, include, url

from hack import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index" ),
		
    url(r'^solve/$', views.solve, name="solve" ),
    url(r'^about/$', views.about, name="about" ),
    url(r'^contact/$', views.contact, name="contact" ),
    url(r'^problem/(?P<p_id>\w+)/$', views.problem, name="problem" ),
    url(r'^download/(?P<p_id>\w+)/$', views.download, name="download" ),
    url(r'^upload/(?P<p_id>\w+)/$', views.upload, name="upload" ),
)
