from django import forms
from .models import User

class studentRegistration(forms.Form):
    name=forms.CharField( max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    message=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), max_length=70)