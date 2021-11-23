from rest_framework import serializers, viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """
    Exibe todos os alunos.
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """
    Exibe todos os cursos.
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculasViewSet(viewsets.ModelViewSet):
    """
    Exibe todos as matriculas.
    """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
