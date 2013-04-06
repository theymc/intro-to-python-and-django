# Create your views here.
from movies.api import search_movie
from django.http import *
from django.http.shortcuts import render_to_response

def search_for_movie(request,*args,**kwargs):

	search_term = request.GET.get("search_term")
	if(search_term is None):
		return HttpResponseBadRequest("Please provide the 'search_term' in the GET parameters")

	results = get_movies(search_term)

	return render_to_response("movies.html",results)

def get_movie(request,*args,**kwargs):

	movie_id = request.GET.get('movie_id')
	if(movie_id is None):
		return HttpResponseBadRequest("Please provide 'movie_id' in the GET parameters.")

	try:
		movie = Movie.objects.get(movie_id=request.GET.get("id"))
	except Movie.DoesNotExist:
		return HttpResponseNotFound("Movie with with ")