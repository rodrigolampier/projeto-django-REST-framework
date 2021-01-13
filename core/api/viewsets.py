from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication


class PontoTuristicoViewSet(ModelViewSet):
    # Faz uma query full nos registros do model PontoTuristico
    queryset = PontoTuristico.objects.all()
    # Chama a função de serialização dos registros
    serializer_class = PontoTuristicoSerializer

    # Outra maneira de fazer buscas
    filter_backends = (SearchFilter,)
    search_fields = ('^nome', '^descricao')

    # Autenticação
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)

    # Usando string query para filtar as informações
    # Isso é uma string query: http://127.0.0.1:8000/pontoturistico/?id=1&&nome=%Pedra%&descricao=%
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = PontoTuristico.objects.filter(nome__iexact=nome)

        if descricao:
            queryset = PontoTuristico.objects.filter(descricao__iexact=descricao)

        return queryset

    """"
        Sobrescrevendo métodos (actions) padrões herdados da ModelViewSet
        Pode ser útil quando quisemos implementar uma lógica personalizada nas ações padrões


    # Retorna apenas os pontos previamente aprovados
    # sobrescreve a nossa ação que tinhamos ali em cima, queryset
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)


    # Essa é a função padrão (do ModelViewSet) de listar tudo (get)
    def list(self, request, *args, **kwargs):
        # Implementariamos aqui...
        return Response({'teste': 123})

    # Essa é a função padrão (do ModelViewSet) de cadastrar algo (put)
    def create(self, request, *args, **kwargs):
        # Implementariamos aqui...
        return Response({'teste': 123})

    # Essa é a função padrão (do ModelViewSet) de deleta algo (del)
    # Boa prática é não deletar o registro no banco, mas apenas desabilita-lo
    def destroy(self, request, *args, **kwargs):
        # Implementariamos aqui...
        return Response({'teste': 123})

    def retrieve(self, request, *args, **kwargs):
        # Implementariamos aqui...
        return Response({'teste': 123})

    # Essa é a função padrão (do ModelViewSet) de atualiza 1 recurso (put)
    def update(self, request, *args, **kwargs):
        # Implementariamos aqui...
        return Response({'teste': 123})

    def partial_update(self, request, *args, **kwargs):
        # Implementariamos aqui...
        return Response({'teste': 123})

"""
