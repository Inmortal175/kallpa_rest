
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import  ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from user.user_serializers.serializers import RegisterClientSerializer, UserSerializer, UserDetailSerializer
from user.user_serializers.serializers import ClientUserUpdateSerializer
from user.models import User

class RegisterClientView(APIView):
  def post(self, request):
    serializer = RegisterClientSerializer(data = request.data)

    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status = status.HTTP_200_OK)
    
    return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

class UserView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request):
    serializer = UserSerializer(request.user)
    return Response(status = status.HTTP_200_OK, data = serializer.data)

  def put(self, request):
    user = User.objects.get(id=request.user.id)
    serializer = ClientUserUpdateSerializer(user, request.data)

    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(status=status.HTTP_200_OK, data = serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST, data = serializer.errors)

class AllUsersView(ModelViewSet):
  permission_classes = [IsAdminUser]
  serializer_class = UserDetailSerializer
  queryset = User.objects.all()
  http_method_names = ["get"]