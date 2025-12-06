from rest_framework import serializers
from .models import *

class MovieSerializer(Serializers.ModelSrializers):
    class Meta:
        model = Movie
        fields = '__all__'
