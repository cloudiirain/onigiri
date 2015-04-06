from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'onigiri.views.home', name='home'),
    url(r'^directory/', include('directory.urls')),
]
