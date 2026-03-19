from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
class Current_leader(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='leaders', blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    id_no = models.CharField(max_length=10)
    course = models.CharField(max_length=50)
    year_discharged = models.CharField()

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=10)

    def __str__(self):
        return self.name
                           
