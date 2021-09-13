from django import forms

from .models import Tech

class TechForm(forms.ModelForm):

    class Meta:
        model = Tech
        fields = ('tech', 'tech_number', 'reason')