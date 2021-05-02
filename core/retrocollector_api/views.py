from rest_framework.decorators import api_view
from rest_framework.response import Response
from retrocollector.models import Collectible, Type
from .serializers import CollectibleSerializer, TypeSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def collectible_api(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            c = Collectible.objects.get(id=pk)
            serializer = CollectibleSerializer(c)
            return Response(serializer.data)
        col = Collectible.objects.all()
        serializer = CollectibleSerializer(col, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CollectibleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ({'msg':'Collectible Added'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        c = Collectible.objects.get(id=pk)
        serializer = CollectibleSerializer(c, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)

    if request.method =='DELETE':
        c = Collectible.objects.get(id=pk)
        c.delete()
        return Response({'msg': 'Collectible Deleted'})


@api_view(['GET', 'POST', 'DELETE'])
def type_api(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            c = Type.objects.get(id=pk)
            serializer = TypeSerializer(c)
            return Response(serializer.data)
        t = Type.objects.all()
        serializer = TypeSerializer(t, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Type Added'})
        return Response(serializer.errors)

    if request.method == 'DELETE':
        c = Type.objects.get(id=pk)
        c.delete()
        return Response({'msg': 'Type Deleted'})
