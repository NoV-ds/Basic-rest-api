from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-details')
    class Meta:
        model = UserDetails
        fields = ['url', 'id', 'name', 'email', 'community']

# class UserdeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         fields = ['name', 'email', 'community']
#         extra_fields = {
#             'url':{'view_name', 'name', 'lookup_field', 'address'},
#             'users':{'lookup_field', 'username'}
#         }