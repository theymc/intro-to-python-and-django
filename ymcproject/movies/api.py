"""
The rotten tomatoes API is documented at: http://developer.rottentomatoes.com/docs
The page follows a search and get flow for a movie.
"""

import requests
from pprint import pprint
API_KEY = "gq6hs44mcn83ghkqehjjftvy"

def get_movies(search_term):
    """
    The GET parameters will be url encoded to make the call. This process
    is explained for the requests library on its official page.
    http://docs.python-requests.org/en/latest/user/quickstart/#passing-parameters-in-urls

    """

    search_url = "http://api.rottentomatoes.com/api/public/v1.0/movies.json"
    params = {
        'apikey': API_KEY,
        'q': search_term,
        'page_limit': 10,
    }

    response = requests.get(search_url,params=params)
    return response.json.get('movies',[])


def get_movie(movie_id):
    """
    The entire movie object will be obtained in this call.
    A sample response has been described in the API documentation.
    """

    movie_url = "http://api.rottentomatoes.com/api/public/v1.0/movies/%s.json"%movie_id
    params = {
        'apikey': API_KEY
    }
    response = requests.get(movie_url,params=params)
    return response.json


def save_movie(movie):

    from models import Movie,Actor,Genre
    
    """
    Save the movie object in your database
    
    Steps:
    1 - First save movie object using only movie_id, title and synopsis
    2 - Iterate through the genres and actors and add them to your movie object.
    3 - Done! 
    
    """
    print "Saving movie %s"%movie['title']
    movie_object,created = Movie.objects.get_or_create(
        movie_id=movie['id'],
        title = movie['title'],
    )
    movie_object.synopsis = movie['synopsis']
    movie_object.save()
    
    for genre in movie['genres']:
        genre_object,created = Genre.objects.get_or_create(name=genre)
        movie_object.genres.add(genre_object)

    for actor in movie['abridged_cast']:
        actor_object,created = Actor.objects.get_or_create(name=actor['name'])
        movie_object.actors.add(actor_object)

def search_and_save(search_term):
    
    search_results = get_movie_ids(search_term)
    
    for movie in search_results:
        movie = get_movie(movie['id'])
        save_movie(movie)

