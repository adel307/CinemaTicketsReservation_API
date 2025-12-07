from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoRestNoModel, name='NoRestNoModel'),
]