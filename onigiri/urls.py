from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'onigiri.views.home', name='home'),
    url(r'^d/', include('directory.urls')),
    url(r'^u/', include('account.urls')),
]
