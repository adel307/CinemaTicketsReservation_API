from django.contrib import admin
from .models import Ticket

# --- Inline Admin for related models ---
# This allows managing Screens directly from the Cinema page.

# --- ModelAdmin Definitions ---

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'screening', 'user', 'status', 'purchase_time')
    list_filter = ('status', 'screening__movie', 'screening__screen__cinema')
    search_fields = ('barcode', 'user__username')
    # Use a custom action to quickly mark tickets as used
    actions = ['mark_as_used']

    @admin.action(description='Mark selected tickets as USED/Checked In')
    def mark_as_used(self, request, queryset):
        updated = queryset.update(status='USED')
        self.message_user(request, f'{updated} tickets were successfully marked as used.', level='success')
