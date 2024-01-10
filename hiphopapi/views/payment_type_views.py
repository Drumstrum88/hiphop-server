from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from hiphopapi.models.payment_type import PaymentType
class PaymentTypeSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = PaymentType
    fields = ('id', 'label')
    
class PaymentTypeView(ViewSet):
  """Get Request for a single payment type"""
  
  def retrieve(self, request, pk):
    
    try:
      paymenttype = PaymentType.objects.get(pk=pk)
      serializer = PaymentTypeSerializer(paymenttype)
      return Response(serializer.data)
    except PaymentType.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  """Get request for all payment types"""
  
  def list(self, request):
    
    try:
      paymenttypes = PaymentType.objects.all()
      serializer = PaymentTypeSerializer(paymenttypes, many=True)
      return Response(serializer.data)
    except PaymentType.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
