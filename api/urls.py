from django.conf.urls import patterns, include, url
from api import views


urlpatterns = patterns('',
    url(r'isbn/(?P<isbn>[0-9]{9})$', views.OfferIsbnSearchView.as_view()),
    url(r'around/(?P<lat>[0-9]{1,3}\.[0-9]{0,10})-(?P<lon>[0-9]{1,3}\.[0-9]{0,10})', views.OfferGeoSearchView.as_view()),
)
