from curso.models import Curso, Disciplina, AreaCientifica
import json
import os
from django.db import transaction

Curso.objects.all().delete()
Disciplina.objects.all().delete()
AreaCientifica.objects.all().delete()

def importar_curso(ficheiro_json):

        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_json = os.path.join(diretorio_atual, ficheiro_json)

        with open(caminho_json, 'r') as f:
            dados_curso = json.load(f)

            with transaction.atomic():
                detalhes_curso = dados_curso['courseDetail']
                curso, created = Curso.objects.get_or_create(
                    nome=detalhes_curso['courseName'],
                    apresentacao=detalhes_curso['presentation'],
                    objetivos=detalhes_curso['objectives'],
                    competencias=detalhes_curso['competences']
                )


                for disciplina_data in dados_curso['courseFlatPlan']:
                    area_cientifica, _ = AreaCientifica.objects.get_or_create(
                        nome=disciplina_data['curricularBranchName']
                    )
                    disciplina, created = Disciplina.objects.get_or_create(
                        nome=disciplina_data['curricularUnitName'],
                        ano=disciplina_data['curricularYear'],
                        semestre=disciplina_data['semester'],
                        ects=disciplina_data['ects'],
                        curricular=disciplina_data['curricularIUnitReadableCode'],
                        area_cientifica=area_cientifica,
                        curso=curso
                    )