from django.db import models

class User(models.Model):
  uid = models.CharField(max_length=50)
  first_name = models.CharField(max_length=50, default='')
  last_name = models.CharField(max_length=50, default='')
