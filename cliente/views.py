from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Compra, Historico
from .forms import ClienteForm, CompraForm, HistoricoForm

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

def nova_compra(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            compra = form.save(commit=False)
            compra.cliente = cliente
            compra.save()
            return redirect('detalhe_cliente', cliente_id = cliente.id)
    else:
        form = CompraForm()
    return render(request, 'cliente/nova_compra.html', {'cliente': cliente, 'form': form })

def remove_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'cliente/remover_cliente.html', {'cliente': cliente})

def remove_compra(request, cliente_id, compra_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    compra = get_object_or_404(Compra, id=compra_id)
    if request.method == 'POST':
        compra.delete()
        return redirect('detalhe_cliente', cliente_id=cliente_id)
    return render(request, 'cliente/remover_compra.html', {'cliente': cliente, 'compra': compra})

def remover_todas_compras(cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    compra = Compra.objects.filter(cliente=cliente)
    for compras in compra:
        compras.delete()

def restante_conta(cliente, valor):
    restante_conta = Compra(cliente=cliente, valor=valor)
    restante_conta.save()
    return restante_conta

def pagar_conta(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    compras = Compra.objects.filter(cliente = cliente)

    if request.method == 'POST':
        valorPago = Decimal(request.POST.get('valorPago'))
        total = sum(compra.valor for compra in compras)

        if total > valorPago:
            restante = total - valorPago
            remover_todas_compras(cliente_id)
            restante_conta(cliente, restante)
        else:
            remover_todas_compras(cliente_id)

        return redirect('detalhe_cliente', cliente_id=cliente_id)
    
    return render(request, 'cliente/pagar_conta.html', {'cliente': cliente, 'compras': compras})     