from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao


# Apenas serializa os registros, filtrando os campos desejados
class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'user', 'comentario', 'nota', 'data')
