# Django
from django.urls import path

# Django Rest Framework
from rest_framework.authtoken import views

# Local Models
from tasks.views import TasksList, TasksDetail

urlpatterns = [
  path('', TasksList.as_view()),
  path('<int:pk>', TasksDetail.as_view()),
]