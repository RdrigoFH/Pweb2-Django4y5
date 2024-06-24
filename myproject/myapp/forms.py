from django import forms
from django.core.validators import MinValueValidator

class PersonaForm(forms.Form):
    nombre = forms.CharField(
        required=True,
        label="Nombre",
        initial="Juan",
        help_text="Ingrese su nombre completo",
        error_messages={'required': 'El nombre es obligatorio.'},
        validators=[MinValueValidator(1)],
        widget=forms.TextInput(attrs={'placeholder': 'Nombre'})
    )
    apellido = forms.CharField(
        required=True,
        label="Apellido",
        initial="Pérez",
        help_text="Ingrese su apellido",
        error_messages={'required': 'El apellido es obligatorio.'}
    )
    edad = forms.IntegerField(
        required=False,
        label="Edad",
        help_text="Ingrese su edad (opcional)",
        validators=[MinValueValidator(0)]
    )
    donador = forms.BooleanField(
        required=False,
        label="Donador",
        help_text="Marque si es donador"
    )
