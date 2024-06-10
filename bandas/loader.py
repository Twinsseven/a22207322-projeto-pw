from bandas.models import Banda, Album, Musica
import json

Banda.objects.all().delete()
Album.objects.all().delete()
Musica.objects.all().delete()

with open('bandas/json/bandas.json') as f:
    bandas = json.load(f)

    for banda in bandas:
            Banda.objects.create(
                nome=banda['nome'],
                nacionalidade=banda['nacionalidade'],
                ano_criacao=banda['ano_criacao'],
                numero_membros=banda['numero_membros']
            )

with open('bandas/json/albuns.json') as f:
    albuns = json.load(f)
    for entrada in albuns:
        banda_nome = entrada['banda']
        banda = Banda.objects.get(nome=banda_nome)

        for album_data in entrada.get('albums', []):
            album_obj = Album.objects.create(
                nome=album_data['nome'],
                numero_musicas=len(album_data.get('musicas', [])),  #
                ano_lancamento=album_data['ano_lancamento'],
                banda=banda
            )

            for musica_data in album_data.get('musicas', []):
                Musica.objects.create(
                    nome=musica_data.get('titulo', ''),
                    tipo='',
                    spotify='',
                    duracao=musica_data.get('duracao', ''),
                    album=album_obj
                )