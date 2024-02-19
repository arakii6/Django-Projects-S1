from django.db import models
from .choices import STATE_CHOICES

# Create your models here.
class Student(models.Model):
    # id = models.BigAutoField() This is automatically added by Django. It represents a Primary Key that acts as a counter.
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField()
    file = models.FileField()


class Teacher(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length = 100)


class Cars(models.Model):
    car_name = models.CharField(max_length = 100)
    speed = models.IntegerField(default=50)

    def __str__(self):
        return self.car_name
    


class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    message = models.TextField()
    file = models.FileField(upload_to = 'contact_form_files')


class About(models.Model):
    FName = models.CharField(max_length = 100)
    LName = models.CharField(max_length = 100)
    Email = models.EmailField()
    Address = models.CharField(max_length = 200)
    City = models.CharField(max_length = 50)
    State = models.CharField(max_length = 50, choices = STATE_CHOICES)
    Zip = models.IntegerField()
    File = models.FileField(upload_to = 'about_form_files')