# This Python file uses the following encoding: utf-8
from django import forms
from .models import Desarrollador
from django.forms import ModelForm, Textarea, DateInput, TextInput, NumberInput, SelectDateWidget, CheckboxInput, Select

class DesarrolladorForm(forms.ModelForm):
    class Meta:
        model = Desarrollador
        fields = {'nombre','cumpleanos','imagen','estudios','cv','correo','facebook','instagram','twiter'}
        labels =    {'nombre':'Nombre',
                    'cumpleanos':'Cumpleaños',
                    'estudios':'Estudios',
					'correo':'E-Mail',
                    'facebook':'Facebook',
                    'instagram':'Instagram',
                    'twiter':'Twitter'}
        widgets = {
            'nombre': TextInput(attrs={
                'class':'form-control',
                'id': 'nombre',
                'name': 'nombre',
                'placeholder':'Nombre...'
                }),
            'cumpleanos': SelectDateWidget(attrs={
                'class':'form-control',
                'id': 'cumpleanos',
                'name': 'cumpleanos',
                'placeholder':'Cumpleaños...'
                }),
			'estuidos': TextInput(attrs={
                'class':'form-control',
                'id': 'estudios',
                'name': 'estudios',
                'placeholder':'Estudios...'
                }),
			'correo': TextInput(attrs={
                'class':'form-control',
                'id': 'correo',
                'name': 'correo',
                'placeholder':'E-Mail...'
                }),
            'facebook': TextInput(attrs={
                'class':'form-control',
                'id': 'facebook',
                'name': 'facebook',
                'placeholder':'Facebook...'
                }),
            'instagram': TextInput(attrs={
                'class':'form-control',
                'id': 'instagram',
                'name': 'instagram',
                'placeholder':'Instagram...'
                }),
            'twiter': TextInput(attrs={
                'class':'form-control',
                'id': 'twiter',
                'name': 'twiter',
                'placeholder':'Twitter...'
                }),

        }
