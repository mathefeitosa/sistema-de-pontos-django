import uuid
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from workplaces.models import Workplace


# Create your models here.
class Shift(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, editable=False, primary_key=True
    )
    owner = models.ForeignKey(
        User, verbose_name="Dono", on_delete=models.SET_NULL, null=True
    )
    workplace = models.ForeignKey(
        Workplace,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Local de trabalho",
    )
    begin = models.DateTimeField(
        auto_now=False, auto_now_add=True, verbose_name="Início"
    )
    end = models.DateTimeField(
        default=None, auto_now=False, auto_now_add=False, verbose_name="Fim", null=True, blank=True
    )
    begin_position = models.CharField(
        max_length=200, verbose_name="Posição no início")
    end_position = models.CharField(
        max_length=200, verbose_name="Posição no fim", blank=True)
    begin_photo = models.ImageField(
        upload_to="static/shift_photos", verbose_name="Foto de entrada", blank=True, null=True
    )
    end_photo = models.ImageField(
        upload_to="static/shift_photos", verbose_name="Foto de saída", blank=True, null=True
    )
    is_open = models.BooleanField(
        default=True, verbose_name="Ponto está em aberto?")

    def __str__(self):
        return f"{self.is_open} | {self.begin.ctime()} | {self.workplace.name} | {self.owner.username}"


@receiver(pre_delete, sender=Shift)
def pre_delete_shift(sender, instance, **kwargs):
    # deleta as fotos associadas
    if instance.begin_photo:
        instance.begin_photo.delete()
    if instance.end_photo:
        instance.end_photo.delete()
