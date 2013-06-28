from django.conf.urls import patterns, include, url

from restaurantsystem.views import get_product_updated_price

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'goodfood.views.home', name='home'),
    # url(r'^goodfood/', include('goodfood.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/restaurantsystem/getupdatedprice/(\d+)/$', get_product_updated_price),
)
