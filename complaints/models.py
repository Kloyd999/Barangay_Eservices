from django.db import models
from residents.models import Resident
# Create your models here.

class Complaint(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('rejected', 'Rejected'),
    )

    complainant = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='complaints_made')
    respondent_name = models.CharField(max_length=200)
    complaint_details = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.respondent_name