from rest_framework import serializers
from django.shortcuts import get_object_or_404
from books.models import Book, Gender
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = ["id", "name"]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "User Serializer",
            summary="Criação de books",
            description="Rota para criação de books",
            value={
                "title": "O Pequeno Príncipe",
                "author": "Antoine de Saint-Exupéry",
                "description": "O pequeno príncipe é um dos maiores clássicos da literatura francesa.",
                "pages": 50,
                "book_genders": [{"name": "Ficção Francesa"}],
            },
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            "User Serializer",
            value={
                "id": 1,
                "title": "O Pequeno Príncipe",
                "author": "Antoine de Saint-Exupéry",
                "description": "O pequeno príncipe é um dos maiores clássicos da literatura francesa.",
                "pages": 50,
                "book_genders": [{"name": "Ficção Francesa"}],
                "followers": [
                    {"id": 1, "username": "João", "email": "joão@dev.com"},
                    {"id": 2, "username": "Pedrinho", "email": "Pedrinho@dev.com"},
                ],
            },
            request_only=False,
            response_only=True,
        ),
    ]
)
class BookSerializer(serializers.ModelSerializer):
    book_genders = GenderSerializer(many=True)

    def create(self, validated_data: dict) -> Book:
        gender_list = validated_data.pop("book_genders")

        genders = []

        for gender in gender_list:
            name = gender["name"]
            gender_object = Gender.objects.filter(name__contains=name).first()

            if not gender_object:
                gender_object = Gender.objects.create(name=name)
            genders.append(gender_object)

        book = Book.objects.create(**validated_data)
        book.book_genders.set(genders)
        return book

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "description",
            "pages",
            "created_at",
            "updated_at",
            "followers",
            "book_genders",
        ]
        depth = 1
