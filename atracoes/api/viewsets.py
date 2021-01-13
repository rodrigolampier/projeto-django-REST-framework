from rest_framework.viewsets import ModelViewSet
from core.models import Atracao
from .serializers import AtracaoSerializer
from django_filters import rest_framework as filters


class AtracaoViewSet(ModelViewSet):
    # Faz uma query full nos registros do model PontoTuristico
    queryset = Atracao.objects.all()
    # Chama a função de serialização dos registros
    serializer_class = AtracaoSerializer

    # Realizando filtros com o django_filters
    filter_backends = (filters.DjangoFilterBackend,)
    # Campos que vão ser pesquisáveis
    filter_fields = ('nome', 'descricao')
