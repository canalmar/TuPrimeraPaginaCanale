from django import forms
from .models import Client


class ClientForm(forms.ModelForm):
    """ Formulario Bootstrap para crear/editar clientes.
    Incluye nombre, apellido, e-mail y teléfono."""
    
    class Meta:
        model = Client
        fields = ["first_name", "last_name", "email", "phone"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name":  forms.TextInput(attrs={"class": "form-control"}),
            "email":      forms.EmailInput(attrs={"class": "form-control"}),
            "phone":      forms.TextInput(attrs={"class": "form-control"}),
        }
