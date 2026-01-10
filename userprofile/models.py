from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userprofile(models.Model):
    userr = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to="userprofile", null=True, blank=True)
