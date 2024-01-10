from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status, serializers
from hiphopapi.models.item import Item
from hiphopapi.models.order import Order
from hiphopapi.models.orderitem import OrderItem

  
class OrderItemSerializer(serializers.ModelSerializer):
    """JSON serializer for an orders items"""
  
    class Meta:
      model = OrderItem
      fields = ('id', 'order', 'item', 'quantity')
    
class OrderItemView(ViewSet):
  
  """GET request for single order item"""
  
  def retrieve(self, request, pk):
    
    try:
      orderitem = OrderItem.objects.get(pk=pk)
      serializer = OrderItemSerializer(orderitem)
      return Response(serializer.data)
    except OrderItem.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  """Get all order items"""
  def list(self, request):
    
    try:
      orderitems = OrderItem.objects.all()
      serializer = OrderItemSerializer(orderitems, many=True)
      return Response(serializer.data)
    except OrderItem.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    """Post request for order items"""
    
  def create(self, request):
      
      order = Order.objects.get(pk=request.data['order'])
      item = Item.objects.get(pk=request.data['item'])
      
      orderitem = OrderItem.objects.create(
        order = order,
        item = item,
        quantity = request.data['quantity']
      )
      
      serializer = OrderItemSerializer(orderitem)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
  """Put request for order items"""
  def update(self, request, pk):
    
    orderitem = OrderItem.objects.get(pk=pk)
    order = Order.objects.get(pk=request.data['order'])
    item = Item.objects.get(pk=request.data['item'])
    
    orderitem.order = order
    orderitem.item = item
    orderitem.quantity = request.data['quantity']
    
    orderitem.save()
    serializer = OrderItemSerializer(orderitem)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  """Delete request for order item"""

def destroy(self, request, pk):
  
  orderitem = OrderItem.objects.get(pk=pk)
  orderitem.delete()
  return Response(None, status=status.HTTP_204_NO_CONTENT)    
    
      
