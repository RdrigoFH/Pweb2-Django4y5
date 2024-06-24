from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

class PersonaForm(forms.Form):
    nombre = forms.CharField(
        required=True,
        label="Nombre",
        initial="Juan",
        help_text="",
        error_messages={'required': 'El nombre es obligatorio.'},
        validators=[MinValueValidator(1)],
        widget=forms.TextInput(attrs={'placeholder': 'Nombre'})
    )
    apellido = forms.CharField(
        required=True,
        label="Apellido",
        initial="Pérez",
        help_text="",
        error_messages={'required': 'El apellido es obligatorio.'}
    )
    edad = forms.IntegerField(
        required=False,
        label="Edad",
        help_text="",
        validators=[MinValueValidator(0)]
    )
    donador = forms.BooleanField(
        required=False,
        label="Donador",
        help_text=""
    )

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
