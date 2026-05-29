from ..data.repository.documento_repository import DocumentoRepository


class DocumentoController:
    
    def __init__(self):
        self.repository = DocumentoRepository()
    
    def listar_alunos(self) -> list:
        return self.repository.listar_alunos()
    
    def obter_boletim(self, aluno_id: int) -> tuple:
        aluno = self.repository.obter_aluno(aluno_id)
        
        if not aluno:
            return None, "Aluno não encontrado"
        
        return aluno, "Boletim carregado com sucesso"
