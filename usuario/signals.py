from django.db.models.signals import post_save
from django.contrib.auth.models import User

from .models import ModelProfile


def teste(sender, instance, created, **kwargs):
    if created:
        profile = ModelProfile.objects.create(usuario=instance)


post_save.connect(teste, sender=User)
