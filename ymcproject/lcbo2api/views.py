from rest_framework import generics
from liquor import models
from serializers import LcboProductSerializer
# from rest_framework import renderers


class LcboList(generics.ListCreateAPIView):
    model = models.LcboProduct
    serializer_class = LcboProductSerializer
    paginate_by = 100
    # renderer_classes = (renderers.XMLRenderer, )


class LcboProduct(generics.RetrieveUpdateAPIView):
    model = models.LcboProduct
    serializer_class = LcboProductSerializer
