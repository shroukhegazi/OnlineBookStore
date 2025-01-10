from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from users.models import CustomUser


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ("id", "username", "email", "password")

    def validate(self, attrs):
        email = attrs.get("email", "").lower()
        username = attrs.get("username", "").lower()

        # Check if email already exists
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": "This email is already in use."}
            )

        # Check if username already exists
        if CustomUser.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"username": "This username is already in use."}
            )

        return super().validate(attrs)
