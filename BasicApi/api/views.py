from django.http import response
from django.shortcuts import redirect, render
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import *

# Create your views here.
@api_view(['GET'])
def apiview(request):
    api_urls = {
        'list': 'user-list/',
        'details': 'user-details/id=/',
        'community': 'user-details/community=/',
        'create' : 'create-user/',
        'update' : 'update-user-details/id= /',
        'delete' : 'delete-user/id=/',
    }

    return Response(api_urls)

@api_view(['GET'])
def userlist(request):
    user = UserDetails.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userdetails(request, pk):
    user = UserDetails.objects.get(pk=pk)
    serializer =UserSerializer(user, many=False)
    return Response(serializer.data)    

@api_view(['GET'])
def userdetailscomm(request, community, *args, **kwargs):
    user = UserDetails.objects.filter(community=community)
    serializer =UserSerializer(user, many=True)
    return Response(serializer.data)    

@api_view(['POST'])
def createuser(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateuser(request, pk):
    user = UserDetails.objects.get(pk=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteuser(request, pk):
    user = UserDetails.objects.get(pk = pk)
    user.delete()
    return Response("User with is successfully deleted")