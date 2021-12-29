# Django Rest Framework
from rest_framework import generics 
from rest_framework.permissions import IsAuthenticated

# Local Models
from tasks.models import Tasks
from tasks.serializers import TasksSerializer


class TasksList(generics.ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = Tasks.objects.all()
  serializer_class = TasksSerializer
    


class TasksDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Tasks.objects.all()
  serializer_class = TasksSerializer