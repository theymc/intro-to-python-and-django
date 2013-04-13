import datetime
from django.views.generic import TemplateView
from movie_master import forms
from django.shortcuts import render
from movies.api import get_movies
from movies.models import Genre
from movie_master.movie_night import make_suggestion


# This is a class based view, using a generic view provided by django
class MovieSearchView(TemplateView):
    template_name = "movies.html"

    def post(self, request, *args, **kwargs):
        form = forms.MovieSearchForm(data=request.POST)
        if form.is_valid():
            search_word = form.cleaned_data.get('movie_name', None)
            context = {'search_results': get_movies(search_word)}
        else:
            # Return the form with errors in the context
            context = {'form': form}

        return render(request, self.template_name, context)

    def get_context_data(self, *args, **kwargs):
        now = datetime.datetime.now()
        return {'current_date': now}


class MovieNightView(TemplateView):

    template_name = "movie_night.html"
    
    def post(self, request, *args, **kwargs):
    
        form = forms.MovieNightForm(data=request.POST)
        if form.is_valid():
            price = form.cleaned_data.get('cost', None)
            genre = form.cleaned_data.get('genre',None)
            alcohol,movie = make_suggestion(int(price),genre)
            context = {
                'data':{
                    'movie': movie,
                    'alcohol': alcohol,
                    'price': "%.2f"%(float(alcohol.price_in_cents)/100),
                }
            }
        else:
            print "Form wasnt valid"
            context = {'form': form}

        return render(request, self.template_name, context)

    def get_context_data(self,*args,**kwargs):
        context = {
            'genre_list':[genre for genre in Genre.objects.all()]
        }
        return context






