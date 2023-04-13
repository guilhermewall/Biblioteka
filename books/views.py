from books.models import Book
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from books.serializers import BookSerializer
from users.permissions import IsCollaboratorOrOwner
from copies.permitions import IsCollaboratorOrReadOnly


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsCollaboratorOrOwner]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        self.check_object_permissions(self.request, serializer.validated_data)
        serializer.save()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsCollaboratorOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
