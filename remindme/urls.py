from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'remindme.views.home', name='home'),
    url(r'^dashboard$', 'remindme.views.dashboard', name='dashboard'),
    url(r'^create$', 'remindme.views.create', name='create'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
]
