from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=8)
    # created_at = models.DateTimeField(auto_now_add=True)
