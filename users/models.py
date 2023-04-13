from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(
        max_length=127,
        unique=True,
        error_messages={
            "unique": "This field must be unique.",
        },
    )

    is_collaborator = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    unlock_date = models.DateField(default=None, null=True)
