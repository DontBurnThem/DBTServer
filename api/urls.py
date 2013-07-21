from django.conf.urls import patterns, include, url
from api import views


urlpatterns = patterns('',
    url(r'isbn/(?P<isbn>\d{9})$', views.OfferIsbnSearchView.as_view()),
    url(r'around-(?P<distance>\d*)/(?P<lat>\d{1,3}\.\d{0,10})-(?P<lon>\d{1,3}\.\d{0,10})', views.OfferGeoSearchView.as_view()),
)
