from django.db import models

class PaymentType(models.Model):
  label = models.CharField(max_length=50)
