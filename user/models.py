from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Sellar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sellar')
    is_sellar = models.BooleanField(default=False)

