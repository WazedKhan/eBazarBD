from django.db.models.signals import post_save
from django.dispatch import receiver
from sellers.models import Seller
from django.conf import settings


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def createSeller(sender, instance, **kwargs):
    if instance.is_seller:
        Seller.objects.create(user = instance)
