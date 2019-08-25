from django.urls import path, include
from rest_framework import routers

from infraestrutura.api.viewsets import OcorrenciaViewSet

router = routers.DefaultRouter()
router.register(r'ocorrencia', OcorrenciaViewSet, base_name="ModelOcorrencia")

urlpatterns = [
    path('', include(router.urls)),
]
