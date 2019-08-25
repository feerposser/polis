from django.db import models
from django.contrib.auth.models import User


class ModelComentario(models.Model):

    COMENTARIO_ESTADO_CHOICES = (
        ("D", "DELETADO"),
        ("A", "ATIVO"),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    criacao = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=8, choices=COMENTARIO_ESTADO_CHOICES)

    class Meta:
        db_table = 'comentario'
        verbose_name = 'Comentario'
        verbose_name_plural = "Comentários"

    def __str__(self):
        return self.usuario.username + " - " + str(self.criacao)

    def delete(self, using=None, keep_parents=False):
        self.estado = "DELETADO"
        self.save()


class ModelOcorrenciaCategoria(models.Model):

    OCORRENCIA_CATEGORIA_ESTADO_CHOICES = (
        ("D", "DELETADO"),
        ("A", "ATIVO"),
    )

    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField()
    criacao = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=8, choices=OCORRENCIA_CATEGORIA_ESTADO_CHOICES)

    class Meta:
        db_table = 'ocorrencia_categoria'
        verbose_name = "Categoria de Ocorrência"
        verbose_name_plural = "Categorias de Ocorrências"

    def __str__(self):
        return self.nome

    def delete(self, using=None, keep_parents=False):
        self.estado = "DELETADO"
        self.save()


class ModelOcorrencia(models.Model):

    STATUS_CHOICES = (
        ("A", "Ativo"),
        ("P", "Pendente de análise"),
        ("R", "Reprovado pela moderação"),
        ("N", "Em andamento"),
        ("P", "Reaberto"),
        ("V", "Revisao"),
    )

    OCORRENCIA_ESTADO_CHOICES = (
        ("D", "DELETADO"),
        ("A", "ATIVO"),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(ModelOcorrenciaCategoria, on_delete=models.DO_NOTHING)
    comentarios = models.ManyToManyField(ModelComentario, blank=True)
    rua = models.CharField(max_length=150)
    numero = models.CharField(max_length=150, blank=True, null=True)
    bairro = models.CharField(max_length=150)
    setor = models.CharField(max_length=100, blank=True, null=True, help_text="Setor do local. Não mexer.")
    latitude = models.FloatField()
    longitude = models.FloatField()
    descricao = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    criacao = models.DateTimeField(auto_created=True)
    alteracao = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=8, choices=OCORRENCIA_ESTADO_CHOICES)
    foto = models.ImageField(upload_to='ocorrencia', blank=True, null=True)

    class Meta:
        db_table = 'ocorrencia'
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrencias"

    def __str__(self):
        return self.usuario.username + "-" + self.categoria.nome

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.status:
            #todo something
            pass
        super().save()

    def delete(self, using=None, keep_parents=False):
        self.estado = "DELETADO"
        self.save()
