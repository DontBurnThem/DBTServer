from django.conf.urls import patterns, url
from dbtcore import views

urlpatterns = patterns('',
    url(r'^$', views.searchbyisbn, name='searchbyisbn'),
    url(r'^showoffers/', views.showoffers, name='showoffers'),
    url(r'^error/', views.error, name='error'),
)
