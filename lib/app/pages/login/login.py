
import os
from time import sleep
from ...controller import UsuarioController


class Login:
    def __init__(self):
        self.controller = UsuarioController()
    
    def exibir(self) -> bool:
        self._limpar_tela()
        self._exibir_cabecalho()
        
        while True:
            username = input("\nUsuário: ").strip()
            if not username:
                self._limpar_tela()
                print("Usuário precisa de um valor!")
                input("\n[Pressione ENTER para continuar ou CTRL+C para sair!]")
                self._limpar_tela()
                continue
            
            password = input("Senha: ").strip()
            if not password:
                self._limpar_tela()
                print("Senha precisa de um valor!")
                input("\n[Pressione ENTER para continuarou CTRL+C para sair]")
                self._limpar_tela()
                continue
            
            sucesso, mensagem = self.controller.autenticar(username, password)
            
            if sucesso:
                print(f"\n✓ {mensagem}")
                input("\n[Pressione ENTER para continuar ou CTRL+C para sair]")
                return True
            else:
                print(f"\n✗ {mensagem}")
                print("Tente novamente.\n")
    
    def _limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def _exibir_cabecalho(self):
        print("=" * 60)
        print(" " * 20 + "LOGIN")
        print("=" * 60)
        print("\nCredenciais padrão:")
        print("  Usuário: admin")
        print("  Senha: admin")
        print("\n" + "=" * 60)
