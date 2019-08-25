from rest_framework.serializers import ModelSerializer

from infraestrutura.models import ModelOcorrencia


class OcorrenciaSerializer(ModelSerializer):
    class Meta:
        model = ModelOcorrencia
        fields = ('usuario', 'categoria', 'comentarios', 'rua', 'numero', 'bairro', 'setor', 'latitude', 'longitude',
                  'descricao', 'status', 'criacao', 'alteracao', 'estado', 'foto',)
