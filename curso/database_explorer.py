from portfolio.models import Curso, Disciplina, Docente
from django.db.models import Min
from django.db.models import Count
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

def explore_database():
    try:

        print("1. Obter todos os cursos:")
        cursos = Curso.objects.all()
        for curso in cursos:
            print(curso.nome)


        print("\n2. Numero de docentes por curso:")
        numero_docentes_por_curso = Curso.objects.annotate(num_docentes=Count('disciplina__docente')).order_by('num_docentes')
        for curso in numero_docentes_por_curso:
            print(f"{curso.nome}: {curso.num_docentes}")


        print("\n3. Disciplinas com menos de 6 ECTS:")
        disciplinas_menos_ects = Disciplina.objects.filter(ects__lt=6)
        for disciplina in disciplinas_menos_ects:
            print(disciplina.nome)


        print("\n4. Disciplina com o menor número de ECTS:")
        disciplina_menos_ects = Disciplina.objects.aggregate(menor_ects=Min('ects'))
        if disciplina_menos_ects['menor_ects'] is not None:
            disciplina = Disciplina.objects.filter(ects=disciplina_menos_ects['menor_ects']).first()
            print(f"{disciplina.nome} - {disciplina.ects} ECTS")
        else:
            print("Não há disciplinas cadastradas.")


        print("\n5. Docente que ministra o maior número de disciplinas:")
        docente_mais_disciplinas = Docente.objects.annotate(num_disciplinas=Count('disciplinas')).order_by('-num_disciplinas').first()
        if docente_mais_disciplinas:
            print(f"{docente_mais_disciplinas.nome} - {docente_mais_disciplinas.num_disciplinas} disciplinas")
        else:
            print("Não há docentes cadastrados.")


        print("\n6. Curso com o maior número de disciplinas:")
        curso_mais_disciplinas = Curso.objects.annotate(num_disciplinas=Count('disciplina')).order_by('-num_disciplinas').first()
        if curso_mais_disciplinas:
            print(f"{curso_mais_disciplinas.nome} - {curso_mais_disciplinas.num_disciplinas} disciplinas")
        else:
            print("Não há cursos cadastrados.")

    except Exception as e:
        print(f"Ocorreu um erro durante a exploração da base de dados: {e}")
