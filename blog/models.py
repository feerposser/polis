from django.db import models


class ModelContato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField()

    class Meta:
        db_table = 'contato'
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.assunto