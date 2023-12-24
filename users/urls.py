from django.urls import path, include
from djoser.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from rest_framework.routers import SimpleRouter


app_name = UsersConfig.name

users_router = SimpleRouter()

users_router.register("users", UserViewSet, basename="users")
urlpatterns = [
    path("", include(users_router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
