from django import forms

from .models import usuario

class usuarioForm(forms.ModelForm):
    class Meta:
        model= usuario
        fields = (
            'nombre',
            'pais',
            'ciudad',
            'domicilio',
            'sexo',
            'edad',
            'contraseña'
          
        )