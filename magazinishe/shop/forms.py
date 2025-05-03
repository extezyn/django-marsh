from django import forms
from .models import Clothes

class ClothesForm(forms.ModelForm):
    class Meta: 
        model = Clothes
        fields = ['name', 'description', 'price', 'color', 'min_size', 'max_size', 'photo','is_exists','collection', 'category']
        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control'}),
        'price': forms.NumberInput(attrs={'class': 'form-control'}),
        'color': forms.Select(attrs={'class': 'form-control'}),
        'min_size': forms.NumberInput(attrs={'class': 'form-control'}),
        'max_size': forms.NumberInput(attrs={'class': 'form-control'}),
        'photo': forms.FileInput(attrs={'class': 'form-control-file'}),
        'is_exists': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        'collection': forms.Select(attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'}),
    }

