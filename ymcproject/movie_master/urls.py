from django.conf.urls import patterns, include, url
from movie_master import views

urlpatterns = patterns('',
    url(r'^suggest/?$', views.MovieNightView.as_view(), name='suggest'),
    url(r'^/?$', views.MovieSearchView.as_view(), name='home'),  # A function based view
)
