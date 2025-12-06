from rest_framework import serializers
from .models import *

class ScreeningSerializer(Serializers.ModelSrializers):
    class Meta:
        model = Screening
        fields = [
            'pk',
            'tickets',
            'movie',
            'screen',
            'start_time',
            'ticket_price',
        ]
