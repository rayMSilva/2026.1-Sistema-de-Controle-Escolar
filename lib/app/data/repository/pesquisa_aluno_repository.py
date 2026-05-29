from ..provider.aluno_provider import AlunoProvider


class PesquisaAlunoRepository:
    
    def __init__(self):
        self.provider = AlunoProvider()
    
    def buscar_por_nome(self, nome: str) -> list:
        return self.provider.buscar_por_nome(nome)
