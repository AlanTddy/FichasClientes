from django.urls import path
from cliente import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente/', views.lista_clientes, name='lista_clientes'),
    path('cliente/<int:cliente_id>/', views.detalhe_cliente, name='detalhe_cliente'),
    path('cliente/novo/', views.novo_cliente, name='novo_cliente'),
    path('cliente/<int:cliente_id>/nova_compra/', views.nova_compra, name='nova_compra'),
    path('cliente/remover/<int:cliente_id>', views.remove_cliente, name= 'remover_cliente'),
    path('cliente/<int:cliente_id>/remover_compra/<int:compra_id>/', views.remove_compra, name='remover_compra'),
    path('cliente/<int:cliente_id>/pagar_conta', views.pagar_conta, name='pagar_conta'),
    path('cliente/<int:cliente_id>/historico/', views.ver_historico, name='ver_historico'),
]
