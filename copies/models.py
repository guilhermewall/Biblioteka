from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Copy(models.Model):
    ammounts_of_copies = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )
    copies_avaliable = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(1000)],
    )

    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="copies"
    )
    users_loan = models.ManyToManyField(
        "users.User", through="copies.Loan", related_name="copies_loan"
    )


class Loan(models.Model):
    date_receipt = models.DateField(auto_now_add=True)
    date_devolution = models.DateField()
    is_receipt = models.BooleanField(default=False)
    price = models.IntegerField()
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="copy_borrowed"
    )
    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.CASCADE, related_name="user_copy_borrowed"
    )
