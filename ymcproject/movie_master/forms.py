from django import forms

class MovieSearchForm(forms.Form):
    movie_name = forms.CharField()

class MovieNightForm(forms.Form):
    cost = forms.CharField()
    genre = forms.CharField()