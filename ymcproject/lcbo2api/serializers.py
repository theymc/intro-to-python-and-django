from rest_framework import serializers
from liquor import models


class LcboProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LcboProduct
