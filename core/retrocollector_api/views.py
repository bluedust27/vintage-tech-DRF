from rest_framework.decorators import api_view
from rest_framework.response import Response
from retrocollector.models import Collectible
from .serializers import CollectibleSerializer


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
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

