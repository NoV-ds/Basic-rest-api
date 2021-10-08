from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add-user/', getOrCreate.as_view(), name='adduser'),
    path('update-delete/<int:pk>/', updateOrDelete.as_view(), name='updateordelete'),
    path('create/', UserList.as_view(), name='create'),
    path('user/', UserInfoWithMixin.as_view(), name='getdata'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)