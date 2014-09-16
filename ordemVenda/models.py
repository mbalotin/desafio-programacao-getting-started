# -*- coding: utf-8 -*-
from django.db import models

class OrdemDeVenda(models.Model):
    nomeComprador = models.CharField(max_length=20, null= False);
    qtde = models.PositiveIntegerField(null=False)
    descricaoItem = models.CharField(max_length=50, null=False);
    valorItem = models.DecimalField(max_digits=10, decimal_places=2);
    totalBruto = models.DecimalField(max_digits=20, decimal_places=2);
    nomeVendedor = models.CharField(max_length= 20, null= False)
    enderecoVendedor = models.TextField(max_length=500, null= False);

