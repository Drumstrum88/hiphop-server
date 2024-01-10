from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hiphopapi.models.order import Order
from hiphopapi.models.user import User

class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = ('id', 'cashier_id', 'name', 'order_closed', 'order_type', 'total_amount')
    
    
class OrderView(ViewSet):
  """Order View"""
  
  def retrieve(self, request, pk):
    """GET request for single order"""
    
    try:
      order = Order.objects.get(pk=pk)
      serializer = OrderSerializer(order)
      return Response(serializer.data)
    except Order.DoesNotExist as ex:
      return Response({'message': ex.args[0]},status=status.HTTP_400_BAD_REQUEST)
    
  def list(self, request):
      """GET all orders"""
      
      orders = Order.objects.all()
      serializer = OrderSerializer(orders, many=True)
      return Response(serializer.data)
   
  def create(self, request):
    """Create an order"""
    
    cashier = User.objects.get(pk=request.data['cashier_id'])
    
    order = Order.objects.create(
      cashier = cashier,
      name = request.data["name"],
      order_type = request.data["order_type"],
      total_amount = request.data["total_amount"]
    )
    
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
  def update(self, request, pk):
        """Update an order"""
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error": "Order does not exist"}, status=status.HTTP_404_NOT_FOUND)

        if 'name' in request.data:
            order.name = request.data['name']

        if 'order_type' in request.data:
            order.order_type = request.data['order_type']

        if 'total_amount' in request.data:
            order.total_amount = request.data['total_amount']

        if 'uid' in request.data:
            try:
                cashier = User.objects.get(pk=request.data['uid'])
                order.cashier = cashier
            except User.DoesNotExist:
                return Response({"error": "Cashier does not exist"}, status=status.HTTP_404_NOT_FOUND)

        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

  def destroy(self, request, pk):
        """Delete an order"""
        
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
