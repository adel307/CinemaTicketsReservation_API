from django.db import models
from Movie.models import Movie
from Cinema.models import Screen

# Create your models here.

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='screenings')
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='screenings')
    start_time = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        # Order screenings chronologically by their start time
        ordering = ['start_time']

    def __str__(self):
        # Format the time for readability
        time_str = self.start_time.strftime("%Y-%m-%d %H:%M")
        return f"{self.movie.title} @ {self.screen.cinema.name} ({time_str})"