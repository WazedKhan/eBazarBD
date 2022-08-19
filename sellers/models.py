from django.db import models
from django.conf import settings

class Seller(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='user')
    due = models.FloatField(default=0)
    last_paid = models.FloatField(default=0)
    product_sold = models.IntegerField(default=0)
    product_returned = models.IntegerField(default=0)
    last_paid_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.email

