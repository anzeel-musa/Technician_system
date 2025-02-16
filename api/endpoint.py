from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

def technician_list(request, format=None):
    if request.method == 'GET':
        tech = Technician.objects.all()
        serializer = TechncianSerializers(tech, many=True)
        return JsonResponse({"status": "success", "TotalTechnicians": serializer.data}, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = TechncianSerializers (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return JsonResponse({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET','PUT','DELETE','PATCH', 'HEAD', 'OPTIONS'])    
def technician_detail(request, pk, format=None):    
    if request.method == 'GET':
        try:
            tech = Technician.objects.get(pk=pk)
            serializer = TechncianSerializers(tech)
            return JsonResponse({"Technician": serializer.data})
        except Technician.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
    
    
def technician_detail(request, pk, format=None):    
    if request.method == 'GET':
        try:
            tech = Technician.objects.get(pk=pk)
            serializer = TechncianSerializers(tech)
            return JsonResponse({"Technician": serializer.data})
        except Technician.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
    if request.method == 'PUT':
        try:
            tech = Technician.objects.get(pk=pk)
            serializer = TechncianSerializers(tech, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({"error": serializer.errors}, status.HTTP_400_BAD_REQUEST)
        except Technician.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
        
    if request.method == 'DELETE':
        try:
            tech = Technician.objects.get(pk=pk)
            tech.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Technician.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

