from ..data.repository.listar_alunos_repository import ListarAlunosRepository


class ListarAlunosController:
    
    def __init__(self):
        self.repository = ListarAlunosRepository()
    
    def listar_todos(self) -> list:
        return self.repository.listar_todos()
