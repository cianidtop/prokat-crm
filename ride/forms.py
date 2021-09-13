from django import forms

from .models import Ride

class RideForm(forms.ModelForm):

    class Meta:
        model = Ride
        fields = ('phone_number', 'first_name', 'last_name', 'tech', 'tech_quantity', 'tech_number', 'tariff', 'end_time', 'cena', 'payment_type', 'place_from', 'place_to')