from rest_framework import serializers
from .models import *

class SeatSerializer(Serializers.ModelSrializers):
    class Meta:
        model = Seat
        fields = '__all__'
