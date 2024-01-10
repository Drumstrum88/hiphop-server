from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from hiphopapi.models.order_type import OrderType

class OrderTypeSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = OrderType
    fields = ('id', 'label')
    
    
class OrderTypeView(ViewSet):
  
  """Get request for a single order type"""
  def retrieve(self, request, pk):
    
    try:
      ordertype = OrderType.objects.get(pk=pk)
      serializer = OrderTypeSerializer(ordertype)
      return Response(serializer.data)
    except OrderType.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  """Get request for all order types"""
  
  def list(self, request):
    
    try:
      ordertypes = OrderType.objects.all()
      serializer = OrderTypeSerializer(ordertypes, many=True)
      return Response(serializer.data)
    except OrderType.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
