from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, response
from hiphopapi.models.item import Item
from hiphopapi.models.order import Order
from hiphopapi.models.order_type import OrderType
from hiphopapi.models.orderitem import OrderItem
from hiphopapi.models.user import User
from hiphopapi.views.item_view import ItemSerializer
from hiphopapi.views.order_items_views import OrderItemSerializer

class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for orders"""

    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'name',
            'user',
            'status',
            'customer_phone',
            'customer_email',
            'type',
            'closed',
            'items',
            'user',
        )
        depth = 1 
    
class OrderView(ViewSet):
  """Order View"""
  
  from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hiphopapi.models.item import Item
from hiphopapi.models.order import Order
from hiphopapi.models.orderitem import OrderItem
from hiphopapi.models.user import User
from hiphopapi.views.item_view import ItemSerializer
from rest_framework.decorators import action

class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for orders

    """
    
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ('id', 'name', 'user', 'status', 'customer_phone', 'customer_email', 'type', 'is_closed', 'items', 'user', 'payment','date','tip','total')
        depth = 1
    
class OrderView(ViewSet):
  """Order View"""
  
  def retrieve(self, request, pk):
    order = Order.objects.get(pk=pk)

    # Fetch order items with related item data
    order_items_with_prices = OrderItem.objects.filter(order=order).select_related('item')
    serializer = OrderSerializer(order, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)


    
  def list(self, request):
      """GET all orders"""
      
      orders = Order.objects.all()
      serializer = OrderSerializer(orders, many=True)
      return Response(serializer.data)
   
  def create(self, request):
    """Create an order"""
    
    user_uid = request.data.get('uid', '')  # Use get method to get the value or an empty string if not present
    
    try:
        user = User.objects.get(uid=user_uid)
    except User.DoesNotExist:
        return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

    # Set default status to 'open' if not present in the request data
    order_status = request.data.get("status", "open")
    
    payment = request.data.get("payment")

    # Get the OrderType instance based on the provided type ID
    type_id = request.data.get("type")
    try:
        order_type = OrderType.objects.get(pk=type_id)
    except OrderType.DoesNotExist:
        return Response({"error": "Order type does not exist"}, status=status.HTTP_404_NOT_FOUND)

    order = Order.objects.create(
        payment=payment,
        user=user,
        name=request.data["name"],
        status=order_status,
        customer_phone=request.data["customer_phone"],
        customer_email=request.data["customer_email"],
        type=order_type, 
        is_closed=request.data.get("is_closed", False),
        
    )
    
    serializer = OrderSerializer(order)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



  from django.shortcuts import get_object_or_404

  from django.shortcuts import get_object_or_404

  def update(self, request, pk):
        """Update an order"""
        order = get_object_or_404(Order, pk=pk)

        update_fields = ['name', 'status', 'customer_phone', 'customer_email', 'type', 'closed', 'uid']

        for field in update_fields:
            if field in request.data:
                if field == 'uid':
                    try:
                        user = User.objects.get(uid=request.data[field])
                        setattr(order, 'user', user)
                    except User.DoesNotExist:
                        return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
                elif field == 'type':
                    try:
                        order_type = OrderType.objects.get(pk=request.data[field])
                        setattr(order, 'type', order_type)
                    except OrderType.DoesNotExist:
                        return Response({"error": "OrderType does not exist"}, status=status.HTTP_404_NOT_FOUND)
                else:
                    setattr(order, field, request.data[field])

        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)


  def destroy(self, request, pk):
        """Delete an order"""
        
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
  
        
  @action(methods=['get'], detail=True)
  def items(self, request, pk):
    """Method to get all the items associated to a single order"""
    items = OrderItem.objects.all()
    orders = items.filter(order_id=pk)
    
    serializer = OrderItemSerializer(orders, many=True)
    return Response(serializer.data)

  