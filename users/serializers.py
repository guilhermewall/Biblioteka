from rest_framework import serializers
from users.models import User

from drf_spectacular.utils import extend_schema_serializer, OpenApiExample


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "User Serializer",
            summary="Criação de usuarios",
            description="Rota para criação de usuarios",
            value={
                "username": "João",
                "email": "joao@dev.com",
                "password": "Senha123",
                "first_name": "Nome",
                "last_name": "Sobrenome",
                "is_collaborator": False,
            },
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            "User Serializer",
            value={
                "id": 1,
                "username": "João",
                "email": "joao@dev.com",
                "password": "Senha123",
                "first_name": "Nome",
                "last_name": "Sobrenome",
                "is_superuser": False,
                "is_collaborator": False,
                "is_blocked": None,
            },
            request_only=False,
            response_only=True,
        ),
    ]
)
class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        if (
            "is_collaborator" in validated_data.keys()
            and validated_data["is_collaborator"]
        ):
            validated_data["is_superuser"] = True

        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_superuser",
            "is_collaborator",
            "is_blocked",
            "unlock_date",
        ]
        extra_kwargs = {"password": {"write_only": True}}
