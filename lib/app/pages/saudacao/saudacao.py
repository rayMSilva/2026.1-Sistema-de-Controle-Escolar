import os

class Saudacao:
    def __init__(self):
        pass
    
    def exibir(self) -> bool:
        try:
            self._limpar_tela()
            self._exibir_cabecalho()
            
            input("\n[Pressione ENTER para continuar ou CTRL+C para sair]")
            return True
            
        except KeyboardInterrupt:
            print("\n\nSistema encerrado. Até logo!")
            return False
    
    def _limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def _exibir_cabecalho(self):
        print("=" * 60)
        print(" " * 15 + "BEM-VINDO AO SISTEMA")
        print(" " * 10 + "CONTROLE ESCOLAR DE NOTAS E ALUNOS")
        print("=" * 60)
        print("\nSistema desenvolvido para gerenciamento de:")
        print("  • Cadastro de Alunos")
        print("  • Registro de Notas")
        print("  • Consulta de Boletins")
        print("  • Pesquisa de Informações")
        print("  • ...")
        print("\n" + "=" * 60)