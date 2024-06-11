from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Compra
from .forms import ClienteForm, CompraForm

def index(request):
    return render(request, 'cliente/index.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/lista_clientes.html', {'clientes': clientes})

def detalhe_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    compras = Compra.objects.filter(cliente=cliente)
    total = sum(compra.valor for compra in compras)
    return render(request, 'cliente/detalhe_cliente.html', {'cliente': cliente, 'compras': compras, 'total': total})

def novo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'cliente/novo_cliente.html', {'form': form})