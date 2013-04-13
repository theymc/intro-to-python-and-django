from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from lcbo2api import views

urlpatterns = patterns('',
    url(r'^lcboproducts/?$', views.LcboList.as_view(), name='lcbo_product_list'),
    url(r'^lcboproducts/(?P<pk>[0-9]+)/?$', views.LcboProduct.as_view(), name='lcbo_product_instance'),
    url(r'^movies/', include('movie_master.urls')),
    url(r'^experiments/', include('experiments.urls')),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
