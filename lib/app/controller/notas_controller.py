from ..data.repository.notas_repository import NotasRepository


class NotasController:
    
    def __init__(self):
        self.repository = NotasRepository()
    
    def lancar_nota(self, aluno_id: int, valor: float) -> tuple:
        
        aluno = self.repository.obter_aluno(aluno_id)
        if not aluno:
            return False, "Aluno não encontrado"
        
        if valor < 0 or valor > 10:
            return False, "Nota deve estar entre 0 e 10"
        
        if len(aluno.notas) >= 2:
            return False, f"Aluno '{aluno.nome}' já possui 2 notas"
        
        if self.repository.adicionar_nota(aluno_id, valor):
            aluno_atualizado = self.repository.obter_aluno(aluno_id)
            return True, f"Nota {valor:.1f} registrada para {aluno.nome}. Média: {aluno_atualizado.media:.2f}"
        else:
            return False, "Erro ao registrar nota"
    
    def listar_alunos(self) -> list:
        return self.repository.listar_alunos()
    
    def obter_aluno(self, aluno_id: int):
        return self.repository.obter_aluno(aluno_id=aluno_id)
