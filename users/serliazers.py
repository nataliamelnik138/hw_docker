from rest_framework import serializers

from courses.serliazers import PaymentSerializer
from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password',)


class UserSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'avatar', 'phone', 'city', 'payment',)


class UserPublicSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'email', 'avatar', 'city',)
