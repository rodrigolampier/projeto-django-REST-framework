from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer


# Apenas serializa os registros, filtrando os campos desejados
class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)  # Usamos many quando temos relação de 1 para muitos
    enderecos = EnderecoSerializer()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado',
                  'foto', 'atracoes', 'comentarios',
                  'avaliacoes', 'endereco')
