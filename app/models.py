from django.db import models

# Create your models here.
# accounts/models.py

from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    # Custom fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_doctor = models.BooleanField('Is doctor',default=False)
    is_patient = models.BooleanField('Is patient',default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    username = models.CharField(max_length=100 ,unique=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
