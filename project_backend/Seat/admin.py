from django.contrib import admin
from .models import Seat

# Register the remaining model (Seat) simply
@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('screen', 'row', 'number')
    list_filter = ('screen__cinema',)
    search_fields = ('row', 'number')