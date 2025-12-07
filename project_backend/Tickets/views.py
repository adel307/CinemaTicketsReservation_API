from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Ticket

# Create your views here.

#1 without rest and no model quary FBV
def NoRestNoModel(request):
    guests = [
        {
            'name':'adel',
            'phone':'011157',
            'address':'adel-adress',
        },
        {
            'name':'ali',
            'phone':'011156',
            'address':'ali-adress',
        },
        {
            'name':'ahmed',
            'phone':'011153',
            'address':'ahmed-adress',
        },
    ]
    return JsonResponse (guests,safe = False)

#1 model data defualt django without rest
def NoRestFromModel(request):
    data = Ticket.objects.all()
    response = {
        'Tickets':list(data.values())
    }

    return JsonResponse (response)
