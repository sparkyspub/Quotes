from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class UserManager(models.Manager):
#     def login(self, postData):

class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)

class Quote(models.Model):
    quotes = models.CharField(max_length = 500)

    # objects = UserManager()
