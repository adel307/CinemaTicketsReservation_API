from django.db import models
from Screening.models import Screening
from Seat.models import Seat


# Choices for ticket status
TICKET_STATUS_CHOICES = [
    ('PENDING', 'Pending Payment'),
    ('CONFIRMED', 'Confirmed'),
    ('USED', 'Used/Checked In'),
    ('CANCELLED', 'Cancelled'),
]

# Create your models here.
class Ticket(models.Model):
    # Link to the screening time/location
    screening = models.ForeignKey(Screening, on_delete=models.PROTECT, related_name='tickets')
    
    # Optional: Link to the specific seat if you used the Seat model
    seat = models.ForeignKey(
        Seat, 
        on_delete=models.PROTECT, 
        related_name='tickets',
        blank=True, 
        null=True
    )
    
    # Link to the user who purchased the ticket (assuming you have a User model)
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='tickets') 
    
    # Unique code for checking/scanning the ticket
    barcode = models.CharField(max_length=32, unique=True)
    
    # The current status of the ticket
    status = models.CharField(
        max_length=10, 
        choices=TICKET_STATUS_CHOICES, 
        default='CONFIRMED'
    )
    
    purchase_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Ticket {self.barcode} for {self.screening.movie.title}"