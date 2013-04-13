from movies.models import *
from liquor.models import *


def get_random_genre():

	genres = Genre.objects.all().order_by("?")
	return genres[0].name

def get_best_alcohol(price,liquor_type):
	price *= 10
	liquors = LcboProduct.objects.filter(
		price_in_cents__lte=price,
		primary_category=liquor_type).order_by("-alcohol_content")

	try:	
		return liquors[0]
	except IndexError:
		return LcboProduct.objects.filter(
			price_in_cents__lte=price).order_by("?")[0]

def match_movie_genre(genre):

	matching = 	{
		'Action & Adventure': 'Beer',
		'Animation': 'Non-Alcoholic',
		'Art House & International': 'Wine',
		'Classics': 'Wine',
		'Comedy': 'Beer',
		'Drama': 'Wine',
		'Horror': 'Spirits',
		'Kids & Family': 'Non-Alcoholic',
		'Mystery & Suspense': 'Spirits',
		'Romance': 'Wine',
		'Science Fiction & Fantasy': 'Beer',
		'Documentary': 'Ready-to-Drink/Coolers',
		'Musical & Performing Arts': 'Cider',
		'Special Interest': 'Beer',
		'Sports & Fitness': 'Non-Alcoholic',
		'Television': 'Beer',
		'Western': 'Beer',
	}

	return matching.get(genre,'Beer')

def get_random_movie_for_genre(genre):

	movies = Movie.objects.all().order_by("?")
	if(movies.filter(genres__name=genre).count()):
		return movies.filter(genres__name=genre)[0]
	else:
		return movies[0]

def make_suggestion(price,genre):
	
	liquor_type = match_movie_genre(genre)
	best_alcohol = get_best_alcohol(price,genre)
	movie = get_random_movie_for_genre(genre)

	return best_alcohol,movie

