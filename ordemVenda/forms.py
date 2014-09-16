# -*- coding: iso-8859-1 -*-
from django import forms

class FormOrdemVenda(forms.Form):
    comprador = forms.CharField(label='Comprador', max_length=20 )
    descricaoItem= forms.CharField(max_length=50, label='Item')
    valor= forms.DecimalField(min_value = 0,max_digits=10, decimal_places=2, label='Valor')
    qtde=forms.IntegerField(min_value = 0, label="Quantidade")
    endereco= forms.CharField(max_length=500 ,widget=forms.Textarea, label='Endereço')
    vendedor = forms.CharField(max_length=20, label='Nome')
