from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from ckeditor.widgets import CKEditorWidget
from .models import Recipe


class NewRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['category', 'name', 'description', 'image',]

    category = forms.Select(attrs={
        'placeholder': 'Tarif Türü',
        'class': 'form-select'
    })

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Tarif Başlığı',
        'class': 'form-control'
    }))

    description = forms.CharField(widget=CKEditorWidget())

    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'class': 'form-control'
    }))


class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = {'category', 'name', 'description', 'image', }
