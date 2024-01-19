from django.db import models
from hiphopapi.models.item import Item
from hiphopapi.models.order import Order

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="order")
    quantity = models.IntegerField(default=0)
