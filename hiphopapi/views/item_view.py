from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hiphopapi.models.item import Item

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = ('id', 'name', 'price')
    
class ItemView(ViewSet):
  """Item View"""
  
  def retrieve(self, request, pk):
    """GET request for single items"""
    
    try:
      item = Item.objects.get(pk=pk)
      serializer = ItemSerializer(item)
      return Response(serializer.data)
    except Item.DoesNotExist as ex:
      return Response({'message' : ex.args[0]},status=status.HTTP_400_BAD_REQUEST)
    
  def list(self, request):
      """GET all items"""
      
      items = Item.objects.all()
      serializer = ItemSerializer(items, many=True)
      return Response(serializer.data)
    
  def create(self, request):
    """Create an Item"""
    
    item = Item.objects.create(
      name = request.data['name'],
      price = request.data['price']
    )
    
    serializer = ItemSerializer(item)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    
  def update(self, request, pk):
    """Update an Item"""
    
    try:
      item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
      return Response({'error': "Item does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    if 'name' in request.data:
      item.name = request.data['name']
     
    if 'price' in request.data:
      item.price = request.data['price']
      
    item.save()
    serializer = ItemSerializer(item)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def destroy(self, request, pk):
    """Delete Item"""
    
    item = Item.objects.get(pk=pk)
    item.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
