__author__ = 'cloudiirain'

from django.conf.urls import include, url, patterns

urlpatterns = patterns('directory',
    url(r'^$', 'views.index', name='index'),
    url(r'^series/new/$', 'views.editseries', name='newseries'),
    url(r'^series/(?P<series_id>\d+)/$', 'views.detail', name='detail'),
    url(r'^series/(?P<series_id>\d+)/edit/$', 'views.editseries', name='editseries'),
    url(r'^volume/new/$', 'views.editvolume', name='newvolume'),
    url(r'^volume/(?P<volume_id>\d+)/edit/$', 'views.editvolume', name='editvolume'),
    url(r'^chapter/new/$', 'views.editchapter', name='newchapter'),
    url(r'^chapter/(?P<chapter_id>\d+)/edit/$', 'views.editchapter', name='editchapter'),
    url(r'^(?P<title>\w+)/$', 'views.title', name='title'),
)
