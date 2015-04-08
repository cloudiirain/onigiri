__author__ = 'cloudiirain'

from django.conf.urls import url, patterns
from directory.views import SeriesListView, SeriesDetailView, SeriesCreate, SeriesUpdate, SeriesDelete
from directory.views import VolumeCreate, VolumeUpdate, VolumeDelete
from directory.views import ChapterCreate, ChapterUpdate, ChapterDelete

urlpatterns = patterns('directory',
    url(r'^$', SeriesListView.as_view(), name='series-list'),
    url(r'^series/(?P<pk>\d+)/$', SeriesDetailView.as_view(), name='series-detail'),
    url(r'^series/new/$', SeriesCreate.as_view(), name='series-add'),
    url(r'^series/(?P<pk>\d+)/edit/$', SeriesUpdate.as_view(), name='series-update'),
    url(r'^series/(?P<pk>\d+)/delete/$', SeriesDelete.as_view(), name='series-delete'),
    url(r'^volume/new/$', VolumeCreate.as_view(), name='volume-add'),
    url(r'^volume/(?P<pk>\d+)/edit/$', VolumeUpdate.as_view(), name='volume-update'),
    url(r'^volume/(?P<pk>\d+)/delete/$', VolumeDelete.as_view(), name='volume-delete'),
    url(r'^chapter/new/$', ChapterCreate.as_view(), name='chapter-add'),
    url(r'^chapter/(?P<pk>\d+)/edit/$', ChapterUpdate.as_view(), name='chapter-update'),
    url(r'^chapter/(?P<pk>\d+)/delete/$', ChapterDelete.as_view(), name='chapter-delete'),
    url(r'^(?P<slug>[\w\-]+)/$', SeriesDetailView.as_view(), name='series-detail-slug'),
    url(r'^(?P<slug>[\w\-]+)/edit$/', SeriesUpdate.as_view(), name='series-update-slug'),
    url(r'^(?P<slug>[\w\-]+)/delete$/', SeriesDelete.as_view(), name='series-delete-slug'),
)
