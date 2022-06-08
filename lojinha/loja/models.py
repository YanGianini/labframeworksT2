from pyexpat import model
from django.db import models
from django.utils import timezone

# Create your models here.
class Pedido(models.Model):
    data_criacao = models.DateTimeField(default=timezone.now),
    valor_total = models.DecimalField(decimal_places=2, max_digits=10)
    ativo = models.BooleanField()

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    qtd_estoque = models.IntegerField()
    preco_unitario = models.DecimalField(decimal_places=2, max_digits=10)
    imagem = models.TextField()
    ativo = models.BooleanField()

class PedidoItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtd = models.FloatField()
    desconto = models.FloatField()
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)


