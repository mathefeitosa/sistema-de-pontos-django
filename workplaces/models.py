from django.db import models
from decimal import Decimal
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Workplaces(models.Model):
  id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
  owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  location = models.CharField(max_length=200)
  turn_size_hours = models.IntegerField()
  hour_price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))
  
  def __str__(self):
    return str(self.name)