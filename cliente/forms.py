from django import forms
from .models import Cliente, Compra, Historico

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'apelido', 'cpf']

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['valor']

class HistoricoForm(forms.ModelForm):
    class Meta:
        model = Historico
        fields = ['valorTotal', 'totalPago']