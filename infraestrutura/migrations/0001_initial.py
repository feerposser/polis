# Generated by Django 2.1.4 on 2019-01-16 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelComentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('D', 'DELETADO'), ('A', 'ATIVO')], max_length=8)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Comentários',
                'db_table': 'comentario',
                'verbose_name': 'Comentario',
            },
        ),
        migrations.CreateModel(
            name='ModelOcorrencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_created=True)),
                ('rua', models.CharField(max_length=150)),
                ('numero', models.CharField(blank=True, max_length=150, null=True)),
                ('bairro', models.CharField(max_length=150)),
                ('setor', models.CharField(blank=True, help_text='Setor do local. Não mexer.', max_length=100, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('descricao', models.TextField()),
                ('status', models.CharField(choices=[('A', 'Ativo'), ('P', 'Pendente de análise'), ('R', 'Reprovado pela moderação'), ('N', 'Em andamento'), ('P', 'Reaberto'), ('V', 'Revisao')], max_length=1)),
                ('alteracao', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('D', 'DELETADO'), ('A', 'ATIVO')], max_length=8)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='ocorrencia')),
            ],
            options={
                'verbose_name_plural': 'Ocorrencias',
                'db_table': 'ocorrencia',
                'verbose_name': 'Ocorrência',
            },
        ),
        migrations.CreateModel(
            name='ModelOcorrenciaCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('descricao', models.TextField()),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('D', 'DELETADO'), ('A', 'ATIVO')], max_length=8)),
            ],
            options={
                'verbose_name_plural': 'Categorias de Ocorrências',
                'db_table': 'ocorrencia_categoria',
                'verbose_name': 'Categoria de Ocorrência',
            },
        ),
        migrations.AddField(
            model_name='modelocorrencia',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='infraestrutura.ModelOcorrenciaCategoria'),
        ),
        migrations.AddField(
            model_name='modelocorrencia',
            name='comentarios',
            field=models.ManyToManyField(blank=True, to='infraestrutura.ModelComentario'),
        ),
        migrations.AddField(
            model_name='modelocorrencia',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
