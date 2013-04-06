from django import forms

class MovieSearchForm(forms.Form):
    movie_name = forms.CharField()