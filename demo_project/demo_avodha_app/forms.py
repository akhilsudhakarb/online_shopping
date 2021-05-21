from .models import shop
from django import forms

class modeForm(forms.ModelForm):
    class Meta:
        model = shop
        fields = ['name', 'price', 'img', 'desc']
