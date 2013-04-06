import datetime
from django.views.generic import TemplateView
from movie_master import forms
from django.shortcuts import render
from movies.api import get_movies


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


