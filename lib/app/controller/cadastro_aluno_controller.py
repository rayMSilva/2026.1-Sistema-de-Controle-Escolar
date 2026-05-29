from ..data.repository.cadastro_aluno_repository import CadastroAlunoRepository
from ..utils import Validador


class CadastroAlunoController:
    def __init__(self):
        self.repository = CadastroAlunoRepository()
        self.validador = Validador()
    
    def cadastrar_aluno(self, nome: str, email: str) -> tuple:
        nome_valido, msg_nome = self.validador.validar_nome(nome)
        if not nome_valido:
            return False, msg_nome
        
        email_valido, msg_email = self.validador.validar_email(email)
        if not email_valido:
            return False, msg_email
        
        if not self.validar_email_unico(email.strip()):
            return False, "Este email já está cadastrado no sistema"
        
        try:
            aluno = self.repository.cadastrar_aluno(nome.strip(), email.strip())
            if aluno:
                return True, f"Aluno '{aluno.nome}' cadastrado com sucesso! Matrícula: {aluno.matricula}"
            else:
                return False, "Erro ao cadastrar aluno"
        except Exception as e:
            return False, f"Erro: {str(e)}"
    
    def validar_email_unico(self, email: str) -> bool:
        return not self.repository.email_existe(email.strip())