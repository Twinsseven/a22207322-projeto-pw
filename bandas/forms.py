from django import forms
from .models import Banda, Album, Musica

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = '__all__'
        help_texts = {
            'nome': 'Digite o nome completo da banda.',
            'biografia': 'Uma breve biografia da banda (máximo de 500 palavras).',
            'numero_membros': 'Número total de membros na banda.',
            'foto_Banda': 'Carregue uma imagem representativa da banda.',
            'nacionalidade': 'País de origem da banda.',
            'ano_criacao': 'Ano em que a banda foi formada.'
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        help_texts = {
            'nome': 'Nome do álbum.',
            'numero_musicas': 'Número total de músicas no álbum.',
            'ano_lancamento': 'Ano de lançamento do álbum.',
            'capa': 'Carregue a capa do álbum.',
            'banda': 'Selecione a banda a qual este álbum pertence.'
        }

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = '__all__'
        help_texts = {
            'nome': 'Nome da música.',
            'tipo': 'Gênero musical da música.',
            'spotify': 'Link do Spotify para esta música.',
            'letra': 'Letras da música (se aplicável).',
            'duracao': 'Duração total da música (formato hh:mm:ss).',
            'album': 'Álbum ao qual esta música pertence.'
        }
