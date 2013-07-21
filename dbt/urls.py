from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
import api

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', api.views.UserViewSet)
router.register(r'books', api.views.BookViewSet)
router.register(r'offers', api.views.OfferViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'api/offers/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^dbtcore/', include('dbtcore.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', include('dbtcore.urls')),
    url(r'^showoffers/', 'dbtcore.views.showoffers'),
    url(r'^$', 'dbtcore.views.searchbyisbn'),
)
