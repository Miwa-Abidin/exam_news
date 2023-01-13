from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    patronymic = models.CharField(max_length=20)


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registered = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.registered}'