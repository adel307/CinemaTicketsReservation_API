from django.urls import path
from . import views

urlpatterns = [
    path('django/NoRestNoModel', views.NoRestNoModel, name='NoRestNoModel'),
    path('django/NoRestFromModel', views.NoRestFromModel, name='NoRestFromModel'),
]