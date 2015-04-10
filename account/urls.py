__author__ = 'jeffrey'

from django.conf.urls import url, patterns, include
from django.contrib.auth import views

urlpatterns = patterns('account',
    url(r'^logout/$', 'views.logout', name='logout'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^register/$', 'views.register', name='register'),
    url(r'^account/$', 'views.dashboard', name='dashboard'),
#    url(r'^search/$', 'views.search', name='search'),

)