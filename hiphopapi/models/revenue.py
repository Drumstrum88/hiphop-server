from django.db import models
from hiphopapi.models.order import Order

class Revenue(models.Model):
  order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
  total_amount = models.DecimalField(max_digits=10, decimal_places=2)
  closure_date = models.DateTimeField(auto_now_add=True)
  tip_amount = models.DecimalField(max_digits=10, decimal_places=2)
