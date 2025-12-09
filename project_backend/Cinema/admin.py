from django.contrib import admin
from .models import Cinema, Screen
from Seat.models import Seat

class ScreenInline(admin.TabularInline):
    model = Screen
    extra = 1 # Number of empty forms to display

class SeatInline(admin.TabularInline):
    model = Seat
    extra = 1

# --- ModelAdmin Definitions ---

@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number')
    search_fields = ('name', 'address')
    # Add Screen management to the Cinema page
    inlines = [ScreenInline] 

@admin.register(Screen)
class ScreenAdmin(admin.ModelAdmin):
    list_display = ('name', 'cinema', 'capacity')
    list_filter = ('cinema',)
    search_fields = ('name',)
    # Add Seat management to the Screen page
    inlines = [SeatInline]