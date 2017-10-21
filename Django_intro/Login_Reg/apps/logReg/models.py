from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

# create a regular expression object for running operations
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

class UserManager(models.Manager):
    def validate_login(self, post_data):
        errors = []
        # check DB for post_data['email']
        if len(self.filter(email=post_data['email'])) > 0:
            # check this user's password
            user = self.filter(email=post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('email/password incorrect')
        else:
            errors.append('email/password incorrect')

        if errors:
            return errors
        return user

    def validate_registration(self, post_data):
        errors = []
        # check length of name fields
        if len(post_data['first_name']) < 2 or len(post_data['last_name']) < 2:
            errors.append("name fields must be at least 3 characters")
        # check length of password
        if len(post_data['password']) < 8:
            errors.append("password must be at least 8 characters")
        # check that name matches settings defined in regex
        if not re.match(NAME_REGEX, post_data['first_name']) or not re.match(NAME_REGEX, post_data['last_name']):
            errors.append('name fields must be letter characters only')
        # check that email matches settings defined in regex
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("invalid email")
        # check to make sure email does not already exist in DB
        if len(User.objects.filter(email=post_data['email'])) > 0:
            errors.append("email is already in use")
        # check password == password_confirm
        if post_data['password'] != post_data['confirm']:
            errors.append("passwords do not match")

        if not errors:
            # hash our password for security
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))
            # create a new user
            new_user = self.create(
                first_name=post_data['first_name'],
                last_name=post_data['last_name'],
                email=post_data['email'],
                password=hashed
            )
            return new_user
        return errors

# create a users table
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    objects = UserManager()
    def __str__(self):
        return self.email
