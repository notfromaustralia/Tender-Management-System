from django.db import models
from datetime import datetime
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

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
    due_date = models.DateField()
    
'''
    Tender detailed document
'''    
class TenderDocument(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    document = models.FileField(upload_to='tender_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)