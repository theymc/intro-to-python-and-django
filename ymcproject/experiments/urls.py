from django.conf.urls import patterns, include, url
from experiments import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^/?$', 'experiments.views.home', name='home'),  # A function based view
    url(r'^classbased/?$', views.TimeView.as_view()),  # A class based view
    # url(r'^ymcproject/', include('ymcproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
