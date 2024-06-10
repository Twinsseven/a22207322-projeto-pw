from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    apresentacao = models.TextField()
    objetivos = models.TextField()
    competencias = models.TextField()

    def __str__(self):
        return self.nome

class AreaCientifica(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=255)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=20)
    ects = models.IntegerField()
    curricular = models.CharField(max_length=20)
    area_cientifica = models.ForeignKey(AreaCientifica, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    disciplina = models.OneToOneField(Disciplina, on_delete=models.CASCADE)
    descricao = models.TextField()
    conceitos_usados = models.TextField()
    tecnologias_usadas = models.TextField()
    imagem = models.ImageField(upload_to='imagens/')
    video = models.URLField()
    github = models.URLField()

    def __str__(self):
        return f"Projeto de {self.disciplina.nome}"


class LinguagemProgramacao(models.Model):
    nome = models.CharField(max_length=50)
    projetos = models.ManyToManyField(Projeto)

    def __str__(self):
        return self.nome

class Docente(models.Model):
    nome = models.CharField(max_length=255)
    disciplinas = models.ManyToManyField(Disciplina)

    def __str__(self):
        return self.nome
