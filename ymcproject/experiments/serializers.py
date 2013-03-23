from rest_framework.serializers import ModelSerializer
from experiments import models


class PersonSerializer(ModelSerializer):
    class Meta:
        model = models.Person