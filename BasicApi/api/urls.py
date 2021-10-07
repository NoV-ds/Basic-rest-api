from django.urls import path

from .views import *

urlpatterns = [
    path('', apiview, name='api_urls'),
    path('user-list/', userlist, name='user-list'),
    path('user-details/id=<int:pk>/', userdetails, name='user-details'),
    path('user-details/community=<str:community>/', userdetailscomm, name='user-details-community'),
    path('create-user/', createuser, name='create-user'),
    path('update-user-details/id=<int:pk>/', updateuser, name='update-userdetails'),
    path('delete-user/id=<int:pk>/', deleteuser, name='delete-user'),
]