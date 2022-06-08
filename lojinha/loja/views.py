from django.shortcuts import render
from loja.models import Produto

# Create your views here.

def index(request):
    produtos = Produto.objects.all()
    return render(request, "index.html", context={'produtos': produtos})

def add(request):
    if request.method == "POST":
        produto = Produto()
        produto.nome = request.POST.get('nome', None)
        produto.qtd_estoque = request.POST.get('qtd', None)
        produto.preco_unitario = request.POST.get('preco', None)
        produto.imagem = request.POST.GET('imagem', None)
        produto.ativo = request.POST.get('ativo', False)
        produto.save()
    return render(request, "add_produto.html")

def busca(request):
    if request.method == "GET":
        srch = request.GET.get('src', None)
        if srch:
            produtos = Produto.objects.filter(nome=srch)
        else:
            produtos = Produto.objects.all()
        print(srch)
        print(produtos)
    return render(request, "result.html", context={'produtos': produtos})