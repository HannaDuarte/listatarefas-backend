from rest_framework import viewsets
from .models import Tarefa
from .serializers import TarefaSerializer

class TarefaViewSet(viewsets.ModelViewSet):
    queryset = Tarefa.objects.all().order_by('-criado_em')
    serializer_class = TarefaSerializer

