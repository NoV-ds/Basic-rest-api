from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins, status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def index(request):
    classapi_urls = {
        'user-list': 'user-list/'
    }
    return Response(classapi_urls)

class getOrCreate(APIView):
    def get(self, request, format=None):
        obj = UserDetails.objects.all()
        serializ = UserSerializer(instance=obj, many=True)
        return Response(serializ.data)

    def post(self, request, format=None):
        serializ = UserSerializer(data=request.data)
        if serializ.is_valid():
            serializ.save()
            return Response(serializ.data, status=status.HTTP_201_CREATED)
        return Response(serializ.errors, status=status.HTTP_400_BAD_REQUEST)

class updateOrDelete(APIView):
    # def get1(self, request, format=None):
    #     obj = UserDetails.objects.all()
    #     serializ = UserSerializer(instance=obj, many=True)
    #     return Response(serializ.data)

    def get(self, pk, format=None):
        obj = UserDetails.objects.get(pk=pk)
        serializ = UserSerializer(instance=obj, many=False)
        return Response(serializ.data)
        
    def put(self, request, pk, format=None):
        id = UserDetails.objects.get(pk=pk)
        serializ = UserSerializer(instance=id, data=request.data)
        if serializ.is_valid():
            serializ.save()
            return Response(serializ.data, status=status.HTTP_201_CREATED)
        return Response(serializ.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        obj = UserDetails.objects.get(pk=pk)
        obj.delete()
        return Response("Successfully Deleted")

    
class UserInfoWithMixin(mixins.RetrieveModelMixin, generics.ListCreateAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    
    # def put(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)
    
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)

class UserList(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = UserDetails.objects.all()
    serializer_class = UserSerializer