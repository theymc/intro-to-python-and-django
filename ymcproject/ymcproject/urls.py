from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from lcbo2api import views

urlpatterns = patterns('',
    # Examples:
    # ? so the slash not necessary
    # $ marks the end of the string
    # name is a way to turn url into a variable
    url(r'^lcboproducts/?$',views.LcboList.as_view(),name='lcbo_product_list'),
    url(r'^lcboproducts/(?P<pk>[0-9]+)/?$',views.LcboList.as_view(),name='lcbo_product_instance'),
    url(r'^movies/', include('movie_master.urls')),
    url(r'^experiments/', include('experiments.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
