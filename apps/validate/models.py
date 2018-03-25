from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z-]{3,20}$')
PASSWORD_REGEX = re.compile(r'^(?=.*[0-9])(?=.*[A-Z])([a-zA-Z0-9!@#$%^&*()]{8,16})$')

class UserManager(models.Manager):
    def register(self, postData):
        errors = {}
        if not NAME_REGEX.match(postData['fname']):
            errors["first_name"] = "First name must be 3-20 characters in length and contain no numbers/special characters"
        if not NAME_REGEX.match(postData['lname']):
            errors["last_name"] = "Last name must be 3-20 characters in length and contain no numbers/special characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email1"] = "Invalid email address entered"
        if User.objects.filter(email=postData['email']):
            errors["email2"] = "Email already exists"
        if postData['password'] != postData['cpassword']:
            errors["password1"] = "Passwords do not match"
        if not PASSWORD_REGEX.match(postData['password']):
            errors["password2"] = "Password must be 8-16 characters, and contain atleast one number and uppercase letter"
        return errors
    def login(self, postData):
        errors = {}
        if not User.objects.filter(email=postData['email']):
            errors["email"] = "Username/email does not exist"
        elif not bcrypt.checkpw(postData['password'].encode(), User.objects.filter(email=postData['email'])[0].password.encode()):
            errors['password'] = "Invalid password entered"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthdate = models.DateTimeField(default="1981-08-31")
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()
    # *************************
