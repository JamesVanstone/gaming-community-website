from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Location(models.Model):
    location_name = models.TextField(max_length=50)

class Mission_Type(models.Model):
    type = models.TextField(max_length=50)

class Mission(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=True)
    pay = models.FloatField(default=0)
    summary = models.TextField(blank=True)
    location = models.ForeignKey(Location, on_delete = models.SET_NULL) # One to many relationship with mission locations.
    type = models.ForeignKey(Mission_Type, on_delete = models.SET_NULL) # One to many relationship with mission types.
    participants = models.ManyToManyField(User, related_name='missions') # Many to many relationship with users