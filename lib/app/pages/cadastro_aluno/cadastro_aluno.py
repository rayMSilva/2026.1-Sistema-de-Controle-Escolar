import os
from ...controller import CadastroAlunoController


class CadastroAluno:
    
    def __init__(self):
        self.controller = CadastroAlunoController()
    
    def exibir(self):
        self._limpar_tela()
        self._exibir_cabecalho()
        
        nome = input("\nNome do aluno: ").strip()
        if not nome:
            print("\n✗ Cadastro cancelado.")
            input("[Pressione ENTER para continuar]")
            return
        
        email = input("Email: ").strip()
        if not email:
            print("\n✗ Cadastro cancelado.")
            input("[Pressione ENTER para continuar]")
            return
        
        
        sucesso, mensagem = self.controller.cadastrar_aluno(nome, email)
        
        if sucesso:
            print(f"\n✓ {mensagem}")
        else:
            print(f"\n✗ {mensagem}")
        
        input("[Pressione ENTER para continuar]")
    
    def _limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def _exibir_cabecalho(self):
        print("=" * 60)
        print(" " * 20 + "CADASTRO DE ALUNO")
        print("=" * 60)
