from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_sellar = models.BooleanField(default=False)
    phone = models.CharField(max_length=12, unique=True)

