from django.db import models

class Actor(models.Model):

	name = models.CharField(max_length=100)

class Genre(models.Model):
	
	name = models.CharField(max_length=100)

class Movie(models.Model):

	movie_id = models.IntegerField()
	title = models.CharField(max_length=100)
	synopsis = models.TextField(blank=True,null=True)
	genres = models.ManyToManyField(Genre)
	actors = models.ManyToManyField(Actor)

	def __unicode__(self):
		return self.title


