from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=70,
        unique=True,
        error_messages={
            "unique": "This field must be unique.",
        })
    author = models.CharField(max_length=127)
    description = models.CharField(max_length=127)
    pages = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    followers = models.ManyToManyField("users.User", related_name="following_books", default=0)
    book_genders = models.ManyToManyField("books.Gender", related_name="books")

    def __repr__(self) -> str:
        return f"<Book[{self.id}]: {self.title}>"


class Gender(models.Model):
    name = models.CharField(
        max_length=50,)

    def __repr__(self) -> str:
        return f"<Gender[{self.id}]: {self.name}>"
