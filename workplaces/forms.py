from django import forms
from .models import Workplace


class WorkplaceForm(forms.ModelForm):
    class Meta:
        model = Workplace
        fields = [
            "owner_profile",
            "name",
            "team",
            "address",
            "location",
            "turn_size_hours",
            "hour_price",
        ]
