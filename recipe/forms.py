from django import forms
from .models import Receita

from django import forms
from .models import Receita

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
       
        fields = ['name', 'ingredients', 'preparationmethod', 'preparationtime', 'fotos']
     
        labels = {
            'name': 'Nome da Receita',
            'ingredients': 'Ingredientes',
            'preparationmethod': 'Modo de Preparo',
            'preparationtime': 'Tempo de Preparo (minutos)',
            'fotos': 'Foto da Receita',
        }