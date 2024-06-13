from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return {self.valor}
    
class Historico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
    totalPago = models.DecimalField(max_digits=10, decimal_places=2)
    dataPagamento = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.totalPago