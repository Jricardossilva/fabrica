from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)

    def _str_(self):
        return f'{self.nome} {self.sobrenome}'



