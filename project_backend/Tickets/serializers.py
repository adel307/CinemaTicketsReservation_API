from rest_framework import serializers
from .models import *

class TicketSerializer(Serializers.ModelSrializers):
    class Meta:
        model = Ticket
        fields = '__all__'
