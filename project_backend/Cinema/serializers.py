from rest_framework import serializers
from .models import *

class CinemaSerializer(Serializers.ModelSrializers):
    class Meta:
        model = cinema
        fields = [
            'pk',
            'screens',
            'name',
            'address',
            'phone_number',

        ]

class ScreenSerializer(Serializers.ModelSrializers):
    class Meta:
        model = Screen
        fields = [
            'pk',
            'screenings',
            'seats',
            'cinema',
            'name',
            'capacity',
        ]
