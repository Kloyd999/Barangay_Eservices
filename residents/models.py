from django.db import models
from authentication.models import User
# Create your models here.

class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=13)
    purok = models.CharField(max_length=100)
    address = models.TextField()
    civil_status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"