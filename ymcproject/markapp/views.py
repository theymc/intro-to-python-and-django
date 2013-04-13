# Create your views here.
from django.shortcuts import render
import datetime

def horse(request,*args,**kwargs):
	context = {
		'current_date': datetime.datetime.now(),
		'horse': True,
	}

	return render(request,"horse.html",context)

