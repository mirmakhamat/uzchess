from rest_framework import serializers
from .models import User, Cart
from library.serializers import BookDetailSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'avatar',
            'email',
            'phone_number',
            'birthdate',
        )


class CartSerializer(serializers.ModelSerializer):
    book = BookDetailSerializer()

    class Meta:
        model = Cart
        fields = (
            'book',
            'quantity',
        )
