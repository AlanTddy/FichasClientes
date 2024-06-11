from django.urls import path
from cliente import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cliente/', views.lista_clientes, name='lista_clientes'),
    path('cliente/<int:cliente_id>/', views.detalhe_cliente, name='detalhe_cliente'),
    path('cliente/novo/', views.novo_cliente, name='novo_cliente'),
]
