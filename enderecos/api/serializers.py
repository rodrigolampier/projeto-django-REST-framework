from rest_framework.serializers import ModelSerializer
from enderecos.models import Endereco


# Apenas serializa os registros, filtrando os campos desejados
class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id', 'linha1', 'linha2', 'cidade', 'estado', 'pais', 'latitude', 'longitude')
