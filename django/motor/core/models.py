from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models .CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    def __str__ (self):
        return f'Nome completo: {self.nome} {self.sobrenome} - e-Mail: {self.email}'


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em Estoque')
    def __str__ (self):
        return f'Produto: {self.nome} - Preco: {self.preco} - Estoque: {self.estoque}'
