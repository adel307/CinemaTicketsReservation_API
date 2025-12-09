from django.contrib import admin
from .models import Screening

@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    list_display = ('movie', 'screen', 'start_time', 'ticket_price')
    list_filter = ('screen__cinema', 'movie', 'start_time')
    search_fields = ('movie__title', 'screen__name')
    # Use date/time hierarchy to easily navigate showtimes
    date_hierarchy = 'start_time' 
