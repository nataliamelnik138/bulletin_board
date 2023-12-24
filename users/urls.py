from django.urls import path, include
# from rest_framework_simplejwt.views import (TokenObtainPairView,
#                                             TokenRefreshView)

from users.apps import UsersConfig


app_name = UsersConfig.name


urlpatterns = [
    path('', include('djoser.urls')),
]
