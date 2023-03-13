from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1)
    lougradouro = models.CharField(max_length=60)
    numero = models.IntegerField()
    setor = models.CharField(max_length=40)
    cidade = models.CharField(max_length=40)
    uf = models.CharField(max_length=2)

class Alergia(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=40)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Vacina(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length=60)
    descricao = models.CharField(max_length=60)
    doses = models.IntegerField()
    periodicidade = models.IntegerField()
    intervalo = models.IntegerField()
    
class Agenda(models.Model):
    id = models.AutoField(primary_key = True)
    data = models.DateField()
    hora = models.CharField(max_length=5)
    situacao = models.CharField(max_length=10)
    data_situacao = models.DateField(null=True, blank=True)
    observacoes = models.CharField(max_length=200, default='')
    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)