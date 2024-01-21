from django.http import HttpResponseServerError
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, response
from hiphopapi.models.item import Item
from hiphopapi.models.order import Order
from hiphopapi.models.order_type import OrderType
from hiphopapi.models.orderitem import OrderItem
from hiphopapi.models.payment_type import PaymentType
from hiphopapi.models.user import User
from hiphopapi.views.item_view import ItemSerializer
from hiphopapi.views.order_items_views import OrderItemSerializer
from hiphopapi.views.payment_type_views import PaymentTypeSerializer

    
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
    items = OrderItemSerializer(many=True, read_only=True)
    payment = PaymentTypeSerializer()  
    date = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = Order
        fields = ('id', 'name', 'user', 'status', 'customer_phone', 'customer_email', 'type', 'is_closed', 'items', 'user', 'payment', 'date', 'tip', 'total')
        depth = 6

    
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
    
    user_uid = request.data.get('uid', '')
    
    try:
        user = User.objects.get(uid=user_uid)
    except User.DoesNotExist:
        return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
   
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
  

  def update(self, request, pk):
    try:
        order = Order.objects.get(pk=pk)

        order.name = request.data.get("name", order.name)
        order.customer_phone = request.data.get("customer_phone", order.customer_phone)
        order.customer_email = request.data.get("customer_email", order.customer_email)

        # Handle the 'type' field separately
        type_data = request.data.get("type")
        type_id = type_data.get("id") if type_data else None

        if type_id is not None:
            order_type = OrderType.objects.get(pk=type_id)
            order.type = order_type

        order.status = "closed"

        # Simplify payment handling
        payment_id = request.data.get("payment")
        order.payment = get_object_or_404(PaymentType, pk=int(payment_id)) if payment_id else None

        order.tip = request.data.get("tip", order.tip)
        order.total = request.data.get("total", order.total)

        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Order.DoesNotExist as ex:
        return Response({'error': str(ex)}, status=status.HTTP_404_NOT_FOUND)
    except OrderType.DoesNotExist as ex:
        return Response({'error': f"Order type with id {type_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except PaymentType.DoesNotExist as ex:
        return Response({'error': f"Payment type with id {payment_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(f"Error during update: {str(e)}")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




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
