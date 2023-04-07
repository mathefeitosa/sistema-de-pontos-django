from django import forms
from .models import Shift
from django.contrib.auth.models import User


class ShiftForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['owner_profile', 'workplace',
                  'begin_position', 'begin_photo']
