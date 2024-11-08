from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Compra, Historico
from .forms import ClienteForm, CompraForm
from django.views.generic import ListView
from django.db.models import Q

def index(request):
    return render(request, 'cliente/index.html')

class ListaCLientesView(ListView):
    model = Cliente
    template_name = 'cliente/lista_clientes.html'
    context_object_name = 'clientes'
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('nome')
        txt_nome = self.request.GET.get('nome')
        if txt_nome:
            queryset = queryset.filter(Q(nome__icontains=txt_nome) | Q(apelido__icontains=txt_nome))
        return queryset

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
            Historico.objects.create(cliente=cliente, valorTotal=total, totalPago=valorPago, restante=restante)
            restante_conta(cliente, restante)
        else:
            remover_todas_compras(cliente_id)
            Historico.objects.create(cliente=cliente, valorTotal=total, totalPago=valorPago, restante=Decimal('0.00'))

        return redirect('detalhe_cliente', cliente_id=cliente_id)
    
    return render(request, 'cliente/pagar_conta.html', {'cliente': cliente, 'compras': compras})     

def ver_historico(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    historico = Historico.objects.filter(cliente=cliente)
    return render(request, 'cliente/historico.html', {'cliente': cliente, 'historico': historico})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == 'POST':
        cliente.nome = request.POST.get('name')
        cliente.apelido = request.POST.get('apelido')
        cliente.cpf = request.POST.get('cpf')
        cliente.save()
        return redirect('detalhe_cliente', cliente_id=cliente_id)
    return render(request, 'cliente/editar.html', {'cliente': cliente})