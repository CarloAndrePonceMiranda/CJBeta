# This Python file uses the following encoding: utf-8
from django import forms
from .models import Plantilla
from django.forms import ModelForm, Textarea, DateInput, TextInput, NumberInput, SelectDateWidget, CheckboxInput, Select
categoria=(('---------','---------'),('Pagina Web','Pagina Web'),('Sistemas Web','Sistemas Web'))

class PlantillaForm(forms.ModelForm):
    class Meta:
        model = Plantilla
        fields = {'nombre','descripcion','categoria','imagen'}
        labels =    {'nombre':'Nombre',
                    'descripcion':'Descripción',
                    'class':'form-control',
                    'categoria':'Categoría'}
        widgets = {
            'nombre': TextInput(attrs={
                'class':'form-control',
                'id': 'nombre',
                'name': 'nombre',
                'placeholder':'Nombre...'
                }),
            'descripcion': TextInput(attrs={
                'class':'form-control',
                'id': 'descripcion',
                'name': 'descripcion',
                'placeholder':'Descripción...'
                }),
            'categoria': forms.Select(attrs={
                'id': 'categoria',
                'class':'form-control',
                'name': 'categoria',
                },choices=categoria),
        }
