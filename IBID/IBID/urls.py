from django.conf.urls import patterns, include, url
from django.contrib import admin
from Home import views

urlpatterns = patterns('',
    url(r'^ideas/', include('ManageIdea.urls',namespace="ManageIdea")),
    url(r'^requests/', include('ManageConnections.urls',namespace="ManageConnections")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('ManageUsers.urls', namespace="ManageUsers")),
    url(r'^$', include('Home.urls',namespace="Home")),
)
