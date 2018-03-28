from __future__ import unicode_literals
from django.db import models
from apps.validate.models import User
import re
import bcrypt
from datetime import datetime
import time

class TripManager(models.Manager):
    def validator(self, postData):
        errors = {}
        today = datetime.today()

        if len(postData['date_from']) > 0: date_from = datetime.strptime(postData['date_from'], "%Y-%m-%d")
        else: date_from = None

        if len(postData['date_to']) > 0: date_to = datetime.strptime(postData['date_to'], "%Y-%m-%d")
        else: date_to = None

        if len(postData['destination']) == 0: errors["destination1"] = "Destination field cannot be empty"
        if Trip.objects.filter(destination=postData['destination'].lower()): errors["destination2"] = "Trip already exists"
        if len(postData['description']) == 0: errors['description'] = "Description field cannot be empty"

        if date_from == None: errors['date_from1'] = "Beginning travel date missing"
        elif date_from < today: errors['date_from2'] = "Beginning travel date must start tomorrow or later"

        if date_to == None: errors['date_to1'] = "Ending travel date missing"
        elif (date_from != None) and (date_to <= date_from): errors['date_to2'] = "Ending travel date must be after beginning travel date"

        return errors
    def edit(self, postData):
        '''errors = {}
        if not User.objects.filter(email=postData['email']):
            errors["email"] = "Username/email does not exist"
        elif not bcrypt.checkpw(postData['password'].encode(), User.objects.filter(email=postData['email'])[0].password.encode()):
            errors['password'] = "Invalid password entered"
        return errors'''
class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    users = models.ManyToManyField(User, related_name="trips")
    travel_date_from = models.DateTimeField(default="1997-08-01")
    travel_date_to = models.DateTimeField(default="1997-08-31")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = TripManager()
    # *************************
