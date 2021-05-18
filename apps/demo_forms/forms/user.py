from django import forms
from ..models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs = {"placeholder": "Nombres Completos"}),
            'password' : forms.PasswordInput(),
            'fecha_nacimiento' : forms.DateInput(
                attrs={
                    'id' : 'datepicker', #habilitar con jQuery
                    'autocomplete' : 'off',
                    'input_format' : "%m/%d/%Y"
                }
            )
        }
        labels = {
           'name': "Nombres",
           'lastname': "Apellidos",
           'fecha_nacimiento': "Fecha de Nacimiento",
           'email': "Correo Electronico",
           'password': "Contraseña"
        }