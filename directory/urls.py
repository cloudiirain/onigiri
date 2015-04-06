__author__ = 'cloudiirain'

from django.conf.urls import url, patterns
from directory.views import SeriesListView, SeriesDetailView, SeriesCreate, SeriesUpdate, SeriesDelete

urlpatterns = patterns('directory',
    url(r'^$', SeriesListView.as_view(), name='series-list'),
    url(r'^series/(?P<pk>\d+)/$', SeriesDetailView.as_view(), name='series-detail'),
    url(r'^series/new/$', SeriesCreate.as_view(), name='series-add'),
    url(r'^series/(?P<pk>\d+)/edit/$', SeriesUpdate.as_view(), name='series-update'),
    url(r'^volume/new/$', 'views.editvolume', name='newvolume'),
    url(r'^volume/(?P<pk>\d+)/edit/$', 'views.editvolume', name='editvolume'),
    url(r'^chapter/new/$', 'views.editchapter', name='newchapter'),
    url(r'^chapter/(?P<pk>\d+)/edit/$', 'views.editchapter', name='editchapter'),
    url(r'^(?P<title>\w+)/$', 'views.title', name='title'),
)
