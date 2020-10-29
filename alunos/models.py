from django.db import models

class Sexo(models.Model):
    descricao = models.CharField(max_length=50)
    sigla = models.CharField(max_length=5)

    def __str__(self):
        return self.descricao

class Alunos(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    dt_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome