from rest_framework.viewsets import ModelViewSet
from enderecos.models import Endereco
from .serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    # Faz uma query full nos registros do model PontoTuristico
    queryset = Endereco.objects.all()
    # Chama a função de serialização dos registros
    serializer_class = EnderecoSerializer
