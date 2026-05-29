import os


class Menu:
    def __init__(self):
        pass
    
    def exibir(self) -> str:
        while True:
            self._limpar_tela()
            self._exibir_opcoes()
            
            opcao = input("\nEscolha uma opção: ").strip()
            
            if opcao in ['1', '2', '3', '4', '5', '6', '7']:
                return opcao
            else:
                print("\n✗ Opção inválida! Tente novamente.")
                input("[Pressione ENTER para continuar]")
    
    def _limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def _exibir_opcoes(self):
        print("=" * 60)
        print(" " * 15 + "SISTEMA DE CONTROLE ESCOLAR")
        print("=" * 60)
        print("\n1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Lançar Notas")
        print("4. Ver Boletim")
        print("5. Buscar Aluno")
        print("6. Remover Aluno")
        print("7. Sair")
        print("\n" + "=" * 60)