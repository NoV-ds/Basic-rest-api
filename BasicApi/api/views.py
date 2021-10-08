from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import *

# Create your views here.
@csrf_exempt
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

@csrf_exempt
@api_view(['GET'])
def userlist(request, format=None):
    user = UserDetails.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
def userdetails(request, pk, format=None):
    user = UserDetails.objects.get(pk=pk)
    serializer =UserSerializer(user, many=False)
    return Response(serializer.data)    

@csrf_exempt
@api_view(['GET'])
def userdetailscomm(request, community, *args, **kwargs):
    user = UserDetails.objects.filter(community=community)
    serializer =UserSerializer(user, many=True)
    return Response(serializer.data)    

@csrf_exempt
@api_view(['POST'])
def createuser(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['PATCH'])
def updateuser(request, pk):
    user = UserDetails.objects.get(pk=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

# @csrf_exempt
# @api_view(['PUT'])
# def Addupdateuser(request):
#     # user = UserDetails.objects.get_or_create(pk=pk)
#     serializer = UserSerializer(UserDetails, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['DELETE'])
def deleteuser(request, pk):
    user = UserDetails.objects.get(pk = pk)
    user.delete()
    return Response("User with is successfully deleted")