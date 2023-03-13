from django.db import models

# Create your models here.
    
class Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=60)
    dt_nasc = models.DateField()
    sexo = models.CharField(max_length=10)
    lougradouro = models.CharField(max_length=60)
    numero = models.IntegerField()
    setor = models.CharField(max_length=40)
    cidade = models.CharField(max_length=40)
    uf = models.CharField(max_length=25)