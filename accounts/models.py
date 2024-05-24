from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(
        '学席番号',
        max_length=8,
        unique=True,
        help_text='学席番号のアルファベットは大文字で入力してください'
    )