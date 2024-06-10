from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=200)
    biografia = models.TextField(default='', null=True, blank=True)
    numero_membros = models.IntegerField(default=0)
    foto_Banda = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, default='0')
    nacionalidade = models.CharField(max_length=100, default='0')
    ano_criacao = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class Album(models.Model):
    nome = models.CharField(max_length=200)
    numero_musicas = models.CharField(max_length=100, default='0')
    ano_lancamento = models.IntegerField(default=0)
    capa = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, default='0')
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='albuns')

    def __str__(self):
        return self.nome

class Musica(models.Model):
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    spotify = models.URLField(max_length=200)
    letra = models.TextField(default='', null=True, blank=True)
    duracao = models.CharField(max_length=200, default='0')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musicas')

    def __str__(self):
        return self.nome
