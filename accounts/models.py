from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    service_no = models.CharField(max_length=50, blank=False)
    course = models.CharField(max_length=100, blank=False)
    year_of_discharge = models.CharField(max_length=50, blank=False)
    employment_status = models.CharField(max_length=100, blank=False)