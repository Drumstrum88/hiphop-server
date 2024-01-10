from django.db import models
from hiphopapi.models.user import User

class Order(models.Model):
  name = models.CharField(max_length=50)
  cashier = models.ForeignKey(User, on_delete=models.CASCADE, default='')
  order_closed = models.BooleanField(default=False)
  order_type = models.CharField(max_length=50)
  total_amount = models.DecimalField(max_digits=10, decimal_places=2)


def __str__(self):
        return f"{self.name} - {self.total_amount}"
