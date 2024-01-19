from django.db import models

from hiphopapi.models.item import Item
from hiphopapi.models.order_type import OrderType
from hiphopapi.models.payment_type import PaymentType
from .user import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=20, default='')
    status = models.CharField(max_length=10, default='open')
    customer_phone = models.CharField(max_length=20, default='')
    customer_email = models.CharField(max_length=20, default='')
    type = models.ForeignKey(OrderType, on_delete=models.CASCADE, null=True)
    tip = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    is_closed = models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True)
    payment = models.ForeignKey(PaymentType, on_delete=models.CASCADE, null=True)
