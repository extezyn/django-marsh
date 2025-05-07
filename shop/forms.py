from django import forms
from .models import Equipment, Order  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class EquipmentForm(forms.ModelForm):
    class Meta: 
        model = Equipment  
        fields = ['name', 'category', 'description', 'price_per_day', 
                 'deposit', 'photo', 'is_available']  
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Велосипед горный'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Описание характеристик инвентаря'
            }),
            'price_per_day': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена за сутки аренды'
            }),
            'deposit': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сумма залога'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'form-control-file',
                'accept': 'image/*'
            }),
            'is_available': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'label': 'Доступен для аренды'
            }),
        }
    
    def clean_price_per_day(self):
        price = self.cleaned_data.get('price_per_day')
        if price <= 0:
            raise forms.ValidationError("Цена должна быть положительной")
        return price
    
    def clean_deposit(self):
        deposit = self.cleaned_data.get('deposit')
        if deposit < 0:
            raise forms.ValidationError("Залог не может быть отрицательным")
        return deposit

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин пользователя',
        min_length=2,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Электроннная почта пользователя',
        min_length=2,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Придумайте пароль пользователя',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин пользователя',
        min_length=2,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Ваш пароль',
        widget= forms.PasswordInput(attrs={'class': 'form-control'})
    )