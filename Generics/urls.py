from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from tasks.views import BookList, BookDetail

urlpatterns = [
    path('api/books', BookList.as_view()),
    path('api/books/<int:pk>', BookDetail.as_view()),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
