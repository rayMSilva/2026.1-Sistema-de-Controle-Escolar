from ..provider.aluno_provider import AlunoProvider


class RemoverAlunoRepository:
    
    def __init__(self):
        self.provider = AlunoProvider()
    
    def listar_alunos(self) -> list:
        return self.provider.obter_todos()
    
    def obter_aluno(self, aluno_id: int):
        return self.provider.obter_aluno(aluno_id)
    
    def deletar_aluno(self, aluno_id: int) -> bool:
        return self.provider.deletar_aluno(aluno_id)
