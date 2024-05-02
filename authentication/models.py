from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SiteUser (models.Model):
    status_choices = [
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
        ('approved', 'Approved'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_registration_no = models.CharField(max_length=100, default='nil')
    mobile_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    kyc_document = models.FileField(upload_to='kyc_docs/', blank=True)
    status = models.CharField(max_length=20, choices=status_choices, default='pending')
    def __str__(self):
        return self.user.username