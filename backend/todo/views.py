from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer, ProfileSerializer
from .models import Todo, ClientProfile

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = ClientProfile.objects.all()
    
    
