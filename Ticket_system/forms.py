from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 19, 'resize': 'none',}))
    class Meta:
        model = Ticket
        exclude = ['status']