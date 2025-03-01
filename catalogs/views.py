from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from catalogs.models import Catalog
from catalogs.serializers import CatalogSerializer


@api_view(['GET', 'POST'])
def catalog_list(request):
    if request.method == 'GET':
        catalogs = Catalog.objects.all()
        serializer = CatalogSerializer(catalogs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CatalogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def catalog_detail(request, pk):
    try:
        catalog = Catalog.objects.get(pk=pk)
    except Catalog.DoesNotExist:
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CatalogSerializer(catalog)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CatalogSerializer(catalog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        catalog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)