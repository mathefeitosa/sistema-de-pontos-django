

from django import forms

from .models import Shift


class ShiftForm(forms.ModelForm):

    class Meta:
        model = Shift
        fields = ['owner', 'workplace', 'end',
                  'begin_position', 'end_position', 'begin_photo', 'end_photo']
        widgets = {
            'end': forms.DateTimeInput(attrs={'type': 'datetime-local'},),
        }
