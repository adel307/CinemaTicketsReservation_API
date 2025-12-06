from django.db import models
from Cinema.models import Screen

# Create your models here.

class Seat(models.Model):
    """Represents a specific seat within a physical Screen."""
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='seats')
    row = models.CharField(max_length=5) # e.g., 'A', 'B'
    number = models.PositiveSmallIntegerField() # e.g., 1, 2, 3

    class Meta:
        # Ensures that a specific (row, number) combination is unique per screen
        unique_together = ('screen', 'row', 'number')

    def __str__(self):
        return f"{self.screen.name} Seat {self.row}{self.number}"