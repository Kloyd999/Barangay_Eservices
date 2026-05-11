from django.db import models
from residents.models import Resident
# Create your models here.

class ServiceRequest(models.Model):

    SERVICE_CHOICES = (
        ('clearance', 'Barangay Clearance'),
        ('indigency', 'Certificate of Indigency'),
        ('residency', 'Certificate of Residency'),
        ('business_permit', 'Business Permit'),
        ('other', 'Other'),
    )

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('completed', 'Completed'),
    )
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    purpose = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    remarks = models.TextField(blank=True, null=True)
    requested_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.resident} - {self.service_type} - {self.status}"