from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import FormOrdemVenda
from models import *
# Create your views here.

def cadastrarVenda(request):
    if request.method == 'POST':
        form=FormOrdemVenda(request.POST)
        if form.is_valid():
            ordem =  OrdemDeVenda()
            ordem.qtde = form.cleaned_data['qtde']
            ordem.nomeComprador = form.cleaned_data['comprador']
            ordem.descricaoItem = form.cleaned_data['descricaoItem']
            ordem.valorItem = form.cleaned_data['valor']
            ordem.enderecoVendedor = form.cleaned_data['endereco']
            ordem.nomeVendedor = form.cleaned_data['vendedor']
            ordem.totalBruto = int(ordem.valorItem) * int(ordem.qtde)
            ordem.save()
            return HttpResponseRedirect('/consulta/')
    else:
        form=FormOrdemVenda()

    return render(request, 'ordemdevenda_create.html', {
        'form': form,
    })
