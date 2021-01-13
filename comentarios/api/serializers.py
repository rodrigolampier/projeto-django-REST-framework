from rest_framework.serializers import ModelSerializer
from comentarios.models import Comentario


# Apenas serializa os registros, filtrando os campos desejados
class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id', 'usuario', 'comentario', 'data', 'aprovado')
