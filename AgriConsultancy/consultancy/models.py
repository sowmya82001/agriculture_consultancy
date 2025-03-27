from django.db import models
from django.contrib.auth.models import User

class Consultant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    expertise = models.CharField(max_length=200)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed')], default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.consultant.name} ({self.date})"

class CropRecommendation(models.Model):
    crop_name = models.CharField(max_length=100)
    soil_type = models.CharField(max_length=200)
    temperature_range = models.CharField(max_length=100)
    rainfall_required = models.CharField(max_length=100)

    def __str__(self):
        return self.crop_name
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
