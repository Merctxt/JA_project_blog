from django import forms
from .models import Comentario
from .models import Contato

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu comentário aqui...',
                'rows': 4,
            }),
        }

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']