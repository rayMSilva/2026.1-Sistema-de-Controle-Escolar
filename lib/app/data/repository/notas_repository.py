from ..models import Aluno
from ..provider.aluno_provider import AlunoProvider


class NotasRepository:
    def __init__(self):
        self.provider = AlunoProvider()
    
    def obter_aluno(self, aluno_id: int) -> Aluno:
        return self.provider.obter_aluno(aluno_id)
    
    def listar_alunos(self) -> list:
        return self.provider.obter_todos()
    
    def adicionar_nota(self, aluno_id: int, valor: float) -> bool:
        return self.provider.adicionar_nota(aluno_id, valor)
