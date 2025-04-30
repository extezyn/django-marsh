from django import forms
from .models import Clothes

class ClothesForm(forms.ModelForm):
    class Meta: 
        model = Clothes
        fields = ['name', 'description', 'price', 'color', 'min_size', 'max_size', 'photo','is_exists','collection', 'category']