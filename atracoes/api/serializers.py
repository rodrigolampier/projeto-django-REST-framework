from rest_framework.serializers import ModelSerializer
from core.models import Atracao


# Apenas serializa os registros, filtrando os campos desejados
class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id', 'nome', 'descricao', 'horario_func', 'idade', 'foto')
