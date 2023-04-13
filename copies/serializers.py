from rest_framework import serializers
from users.serializers import UserSerializer
from books.serializers import BookSerializer
from .models import Copy
from .models import Loan
from datetime import date, timedelta
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Copies Serializer",
            summary="Criação de copias",
            description="Rota para criação de copias",
            value={"ammounts_of_copies": 100, "copies_avaliable": 100, "book": 1},
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            "Copies Serializer",
            value={
                "id": 1,
                "ammounts_of_copies": 100,
                "copies_avaliable": 100,
                "book": {
                    "id": 1,
                    "title": "O Pequeno Príncipe",
                    "author": "Antoine de Saint-Exupéry",
                    "description": "O pequeno príncipe é um dos maiores clássicos da literatura francesa.",
                    "pages": 50,
                    "book_genders": [{"name": "Ficção Francesa"}],
                },
            },
            request_only=False,
            response_only=True,
        ),
    ]
)
class CopySerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> Copy:
        return Copy.objects.create(**validated_data)

    book = serializers.SerializerMethodField()

    class Meta:
        model = Copy
        fields = [
            "id",
            "ammounts_of_copies",
            "copies_avaliable",
            "book",
        ]

    def get_book(self, obj) -> str:
        return obj.book.title


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Loans Serializer",
            summary="Criação de emprestimos",
            description="Rota para criação de emprestimos",
            value={"price": 25, "copy": 1, "user": 1},
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            "Loans Serializer",
            value={
                "id": 0,
                "date_receipt": "2023-03-14",
                "date_devolution": "2023-03-14",
                "is_receipt": False,
                "price": 25,
                "copy": 1,
                "user": 1,
            },
            request_only=False,
            response_only=True,
        ),
    ]
)
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = [
            "id",
            "date_receipt",
            "date_devolution",
            "is_receipt",
            "price",
            "copy",
            "user",
        ]
        read_only_fields = ["id", "date_receipt", "date_devolution"]

    def create(self, validated_data):
        get_date_devolution = date.today() + timedelta(days=10)

        if get_date_devolution.weekday() == 5:
            get_date_devolution += timedelta(days=2)
        elif get_date_devolution == 6:
            get_date_devolution += timedelta(days=1)

        validated_data["date_devolution"] = get_date_devolution

        return Loan.objects.create(**validated_data)
