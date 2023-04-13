from django.urls import path
from books.views import BookView, BookDetailView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/<int:pk>/", BookDetailView.as_view()),
]
