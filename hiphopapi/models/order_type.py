from django.db import models

class OrderType(models.Model):
  label = models.CharField(max_length=50)
