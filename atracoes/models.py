from django.db import models


class Atracao(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    horario_func = models.TextField()
    idade = models.IntegerField()
    # Vai criar essa pasta ai dentro dessa aqui MEDIA_ROOT = 'imagens'
    foto = models.ImageField(upload_to='atracoes', null=True, blank=True)


    def __str__(self):
        return self.nome
