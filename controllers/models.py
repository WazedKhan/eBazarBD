from django.db import models
from users.models import MyUser

class Sellar(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user')
    due = models.FloatField(default=0)
    last_paid = models.FloatField(default=0)
    rate = models.FloatField(default=1.0)
    last_paid_on = models.DateTimeField(auto_now=True)
    company = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return 'Sellar Info'