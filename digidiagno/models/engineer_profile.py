
from django.db import models
from django.contrib.auth.models import User

class EngineerProfile(models.Model):
    userprofile = models.OneToOneField(User, on_delete=models.CASCADE) #unique true bhayechai one to one field hunxa
    designation = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    is_engineer = models.BooleanField(default=True)
    signature = models.ImageField()