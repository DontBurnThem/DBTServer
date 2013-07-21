from django.conf.urls import patterns, include, url
from api import views


urlpatterns = patterns('',
    url(r'^.*$', views.OfferSearchView.as_view()),
)
