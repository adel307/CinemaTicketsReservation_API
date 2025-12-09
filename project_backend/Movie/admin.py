from django.contrib import admin
from .models import  Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration_minutes', 'release_date', 'rating')
    list_filter = ('rating', 'release_date')
    search_fields = ('title', 'description')


