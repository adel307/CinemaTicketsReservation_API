from rest_framework import serializers
from .models import *

class ScreeningSerializer(Serializers.ModelSrializers):
    class Meta:
        model = Screening
        fields = '__all__'
