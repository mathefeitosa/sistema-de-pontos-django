from django.db import models
from decimal import Decimal
from profiles.models import Profile
import uuid

# Create your models here.


class Workplace(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        primary_key=True,
    )
    owner_profile = models.ForeignKey(
        Profile,
        verbose_name="Perfil do usuário",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    name = models.CharField(
        verbose_name='Nome do local',
        max_length=200,
    )
    team = models.CharField(
        verbose_name='Equipe',
        max_length=200,
    )
    address = models.CharField(
        verbose_name='Endereço',
        max_length=200,
    )
    location = models.CharField(
        verbose_name='Localização',
        max_length=200,
    )
    turn_size_hours = models.IntegerField(
        verbose_name='Horas diárias',
    )
    hour_price = models.DecimalField(
        verbose_name='Preço por hora',
        max_digits=6,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    def __str__(self):
        return str(self.name)
