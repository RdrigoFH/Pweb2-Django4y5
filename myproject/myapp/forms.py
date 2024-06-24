from django import forms
from django.core.exceptions import ValidationError
from .models import Persona
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'edad', 'donador']

    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].initial = 'Cristiano'  
        self.fields['apellido'].initial = 'Ronaldo'  

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if nombre and nombre[0] != nombre[0].upper():
            raise ValidationError('La primera letra del nombre debe estar en mayúscula.')
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        if apellido and apellido[0] != apellido[0].upper():
            raise ValidationError('La primera letra del apellido debe estar en mayúscula.')
        return apellido

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad is not None:
            if not isinstance(edad, int):
                raise ValidationError('La edad debe ser un número entero.')
            if edad < 0:
                raise ValidationError('La edad no puede ser negativa.')
        return edad
