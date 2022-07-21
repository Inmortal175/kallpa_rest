from re import U
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.user_views.views import RegisterClientView, UserView, AllUsersView

urlpatterns = [
  path( 'auth/login', TokenObtainPairView.as_view(), name = 'token_obtain_pair'),
  path( 'auth/token/refresh', TokenRefreshView.as_view(), name = 'token_refresh'),
  path( 'auth/register/client', RegisterClientView.as_view(), name = 'register_user'),
  path( 'auth/user', UserView.as_view(), name = 'user_views'),
  path( 'auth/user/details', AllUsersView.as_view({'get':'list'}), name = 'user_views'),
]