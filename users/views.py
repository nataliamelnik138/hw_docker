from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsActivUser
from users.serliazers import UserCreateSerializer, UserSerializer, UserPublicSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self, **kwargs):
        if self.request.user == User.objects.get(pk=self.kwargs.get('pk')):
            self.serializer_class = UserSerializer
        else:
            self.serializer_class = UserPublicSerializer

        return self.serializer_class


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsActivUser]


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserPublicSerializer
    queryset = User.objects.all()
