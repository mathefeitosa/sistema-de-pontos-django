from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User

from profiles.models import Profile


@receiver(post_save, sender=User)
def profile_created(sender, instance, created, **kwargs):
  if created:
    user = instance
    profile = Profile.objects.create(user=user, cpf=user.username)


@receiver(post_delete, sender=Profile)
def profile_deleted(sender, instance, **kwargs):
  user = instance.user
  user.delete()
  pass


def profile_updated():
  pass
