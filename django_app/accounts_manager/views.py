from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import CreateUserSerializer, CustomUserSerializer

from accounts_manager.models import CustomUser


class CreateUserAPIView(APIView):
    def post(self, request, format=None):
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            # Создание пользователя
            user = CustomUser.objects.create_user(username=username, email=email, password=password)
            user.save()
            
            return Response({'message': 'Пользователь успешно создан'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserDetailsView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'user_id'  # Указываем, что параметр в URL будет называться 'user_id'

    def retrieve(self, request, *args, **kwargs):
        try:
            user = self.get_object()
            # Исключаем поле пароля из сериализации
            serializer = CustomUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({'message': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)

# Create your views here.
