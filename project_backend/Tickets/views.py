from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.

#1 with out rest and no model quary FBV
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


