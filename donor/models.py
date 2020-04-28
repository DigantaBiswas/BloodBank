from django.db import models

# Create your models here.

class BloodDonor(models.Model):
    name = models.CharField(max_length=50, null=True)
    blood_group = models.CharField(max_length=10, null=True)
    batch = models.IntegerField(null=True)
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField()
    created_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    fb_url = models.CharField(max_length=50, null=True)
