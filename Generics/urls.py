# Django
from django.contrib import admin
from django.urls import path, include

# Django Rest Framework Token
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/tasks/', include('tasks.urls')),
  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
