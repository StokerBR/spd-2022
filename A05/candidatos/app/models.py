from django.db import models

# Create your models here.
class Candidato(models.Model):
    codigo = models.AutoField(primary_key = True)
    nome = models.CharField(max_length=60)
    sexo = models.CharField(max_length=1)
    data_nasc = models.DateField()
    cargo_pretendido = models.CharField(max_length=25)
    texto_curriculo = models.TextField()