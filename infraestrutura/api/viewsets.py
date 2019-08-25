from rest_framework.viewsets import ModelViewSet

from infraestrutura.models import ModelOcorrencia
from .serializers import OcorrenciaSerializer


class OcorrenciaViewSet(ModelViewSet):
    serializer_class = OcorrenciaSerializer

    def get_queryset(self):
        return ModelOcorrencia.objects.all()
