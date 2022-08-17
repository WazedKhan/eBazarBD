from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import MyUser
from controllers.models import Sellar


# @receiver(request_finished)
# def my_callback(sender, **kwargs):
#     print('Request Finished')

@receiver(post_save, sender = MyUser)
def SellarCreated(sender, instance, **kwargs):
    if instance.is_sellar == True:
        sellar = Sellar.objects.create(user = instance)