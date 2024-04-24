from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SiteUser (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.user.username