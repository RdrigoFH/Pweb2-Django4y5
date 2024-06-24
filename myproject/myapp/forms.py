from django import forms
from django.core.validators import MinValueValidator

class PersonaForm(forms.Form):
    nombre = forms.CharField(
        required=True,
        label="Nombre",
        initial="",
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
