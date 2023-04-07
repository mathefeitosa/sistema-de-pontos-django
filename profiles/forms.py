from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class CreateUserForm(UserCreationForm):
  # Defina os campos adicionais, se necessário
  username = forms.CharField(
      max_length=11,
  )

  class Meta:
    model = User
    fields = [
        'username',
        'password1',
        'password2',
    ]
    labels = {
        'username': 'CPF',
    }


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = [
        'full_name',
        'crm_number',
        'crm_state',
    ]
