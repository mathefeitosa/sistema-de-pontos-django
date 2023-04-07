from django.contrib.auth.models import User
from django.db import models

import uuid

# CONSTANTES
STATE_CHOICES = (
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins"),
)

# MODELOS


class Profile(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Usuário',
    )
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    full_name = models.CharField(
        max_length=200,
        verbose_name='Nome completo',
    )
    cpf = models.CharField(
        max_length=11,
        editable=False,
        verbose_name='CPF',
    )
    crm_number = models.CharField(
        max_length=20,
        verbose_name='Número do CRM',
    )
    crm_state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
        verbose_name='Estado do CRM',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='Data de criação',
    )

    def __str__(self):
        return str(self.full_name)
