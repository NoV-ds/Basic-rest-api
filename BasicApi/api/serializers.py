from rest_framework import serializers
from .models import UserDetails

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=254)
    community = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return UserDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.community = validated_data.get('community', instance.community)
        instance.save()
        return instance