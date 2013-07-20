from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
    url(r'^(?P<isbn>\d+)/$', views.showoffers, name='showoffers')
    url(r'^$', views.searchbyinbn, name='searchbyisbn')
)
