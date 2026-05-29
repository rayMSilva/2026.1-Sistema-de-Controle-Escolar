from ..provider.aluno_provider import AlunoProvider


class ListarAlunosRepository:
    
    def __init__(self):
        self.provider = AlunoProvider()
    
    def listar_todos(self) -> list:
        return self.provider.obter_todos()
