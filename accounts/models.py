from django.db import models
class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_names = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    service_no = models.CharField(max_length=10)
    id_no = models.CharField(max_length=15)  
    course = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)

    address = models.TextField(blank=True)
    bio = models.TextField(blank=True)                   