from django import forms
from .models import Workplaces


class WorkplacesForm(forms.ModelForm):
    class Meta:
        model = Workplaces
        fields = ["owner", "name", "address", 'location', 'turn_size_hours', 'hour_price']
