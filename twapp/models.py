import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Search(models.Model):
   query = models.CharField(max_length=50)
   user = models.ForeignKey(User) 
   def __str__(self):
       return self.query
