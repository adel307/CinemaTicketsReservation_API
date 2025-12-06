from rest_framework import serializers
from .models import *

class CinemaSerializer(Serializers.ModelSrializers):
    class Meta:
        model = cinema
        fields = '__all__'

class ScreenSerializer(Serializers.ModelSrializers):
    class Meta:
        model = Screen
        fields = '__all__'
