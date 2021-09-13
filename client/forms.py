from django import forms

from .models import Client

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('phone_number', 'document', 'document_number', 'document_series', 'first_name', 'last_name', 'middle_name', 'bonus', 'ready', 'sign', 'comment')
