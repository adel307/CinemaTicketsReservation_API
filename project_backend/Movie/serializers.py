from rest_framework import serializers
from .models import *

class MovieSerializer(Serializers.ModelSrializers):
    class Meta:
        model = Movie
        fields = [
            'pk',
            'screenings',
            'title',
            'description',
            'duration_minutes',
            'release_date',
            'rating',
        ]
