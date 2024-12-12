from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Location(models.Model):
    location_name = models.TextField(max_length=50)

    def __str__(self):
        return self.location_name


class Mission_Type(models.Model):
    type = models.TextField(max_length=50)

    def __str__(self):
        return self.type


class Mission(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    pay = models.FloatField(default=0)
    summary = models.TextField(blank=True)
    # One to many relationship with mission locations.
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    # One to many relationship with mission types.
    type = models.ForeignKey(Mission_Type, on_delete=models.PROTECT)
    # Many to many relationship with users
    participants = models.ManyToManyField(User, related_name='missions')
    approved = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Mission " + str(self.date)
