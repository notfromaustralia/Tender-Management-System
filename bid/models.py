from django.db import models
from django.contrib.auth.models import User
from tender.models import Tender
# Create your models here.
class Bid(models.Model):
    status_choices = [
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
        ('approved', 'Approved'),
    ]
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    document = models.FileField(upload_to='tender_proposals/')
    quality_rating = models.IntegerField()
    compliance_rating = models.IntegerField()
    status = models.CharField(max_length=20, choices=status_choices, default='pending')
    # Additional fields as needed 