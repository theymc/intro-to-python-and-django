# Create your views here.
from rest_framework import generics
from liquor import models
from serializers import LcboProductSerializer

class LcboList(generics.ListCreateAPIView):
	model = models.LcboProduct
	serializer_class = LcboProductSerializer
	paginate_by = 100

class LcboProduct(generics.RetrieveUpdateAPIView):
	model = models.LcboProduct
	serializer_class = LcboProductSerializer