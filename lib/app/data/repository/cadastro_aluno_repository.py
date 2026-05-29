from ..models import Aluno
from ..provider.aluno_provider import AlunoProvider


class CadastroAlunoRepository:
    def __init__(self):
        self.alunoProvider = AlunoProvider()
    
    def cadastrar_aluno(self, nome: str, email: str) -> Aluno:
        return self.alunoProvider.criar_aluno(nome, email)
    
    def email_existe(self, email: str) -> bool:
        return self.alunoProvider.email_existe(email)
