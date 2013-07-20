from django.conf.urls import patterns, url
from dbtcore import views

urlpatterns = patterns('',
    url(r'^$', views.searchbyisbn, name='searchbyisbn'),
    # url(r'^(?P<isbn>\d+)$', 'views.showoffers', name='showoffers'),
    url(r'^showoffers.html', views.showoffers, name='showoffers'),
)
