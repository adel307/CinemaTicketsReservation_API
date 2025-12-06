from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration_minutes = models.PositiveSmallIntegerField()
    release_date = models.DateField()
    rating = models.CharField(max_length=10, blank=True) # e.g., 'PG-13', 'R'
    
    def __str__(self):
        return self.title