from rest_framework import serializers
from .models import Todo
from .models import ClientProfile

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = ('fullName', 'address1', 'address2', 'city', 'state', 'zipCode')