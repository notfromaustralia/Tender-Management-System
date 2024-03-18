from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tender(models.Model):
    status_choices = [
        ('assigned', 'Assigned'),
        ('available', 'Available'),
        ('expired', 'Expired'),
    ]
    tender_no = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=status_choices, default='available')
    document = models.FileField(upload_to='tender_documents/')
    publisher = models.ForeignKey(User, on_delete=models.PROTECT,related_name='owned_tenders')
    winner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='won_tenders')
    watchers = models.ManyToManyField(User, related_name='watchlist', blank=True)
    due_date = models.DateField()
    
    def save(self, *args, **kwargs):
        # Check if today's date is greater than the due date
        if datetime.now().date() > self.due_date:
            self.status = 'expired'  # Set status to expired
        super(Tender, self).save(*args, **kwargs) 