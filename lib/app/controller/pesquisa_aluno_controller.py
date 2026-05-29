from ..data.repository.pesquisa_aluno_repository import PesquisaAlunoRepository


class PesquisaAlunoController:
    
    def __init__(self):
        self.repository = PesquisaAlunoRepository()
    
    def buscar_por_nome(self, nome: str) -> list:
        if not nome or len(nome.strip()) == 0:
            return []
        
        alunos = self.repository.buscar_por_nome(nome.strip())
        
        if not alunos:
            return []
        
        return alunos
