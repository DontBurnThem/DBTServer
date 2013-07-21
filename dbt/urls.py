from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from api import views as api_views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', api_views.DBTUserViewSet)
router.register(r'books', api_views.BookViewSet)
router.register(r'offers', api_views.OfferViewSet)

urlpatterns = patterns('',
    url(r'^api/', include(router.urls)),
    url(r'api/offers/search', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^dbtcore/', include('dbtcore.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', include('dbtcore.urls')),
    url(r'^showoffers/', 'dbtcore.views.showoffers'),
    url(r'^error/', 'dbtcore.views.error'),
    url(r'^$', 'dbtcore.views.searchbyisbn'),
    url(r'', include('social_auth.urls')),
)
