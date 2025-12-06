from django.db import models

# Create your models here.

class Cinema(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name

class Screen(models.Model):
    """Represents a specific theater room within a Cinema."""
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='screens')
    name = models.CharField(max_length=50) # e.g., "Screen 1", "IMAX Hall"
    capacity = models.IntegerField()

    class Meta:
        # Ensures that two screens in the same cinema cannot have the same name
        unique_together = ('cinema', 'name')
        
    def __str__(self):
        return f"{self.cinema.name} - {self.name}"
