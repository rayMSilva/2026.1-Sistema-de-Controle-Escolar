from ..data.repository.remover_aluno_repository import RemoverAlunoRepository


class RemoverAlunoController:
    
    def __init__(self):
        self.repository = RemoverAlunoRepository()
    
    def listar_alunos(self) -> list:
        return self.repository.listar_alunos()
    
    def obter_aluno(self, aluno_id: int):
        return self.repository.obter_aluno(aluno_id)
    
    def remover_aluno(self, aluno_id: int) -> tuple:
        aluno = self.repository.obter_aluno(aluno_id)
        
        if not aluno:
            return False, "Aluno não encontrado"
        
        if self.repository.deletar_aluno(aluno_id):
            return True, f"Aluno '{aluno.nome}' removido com sucesso"
        else:
            return False, "Erro ao remover aluno"
