import os
from ...controller.notas_controller import NotasController


class NotasPage:
    def __init__(self):
        self.controller = NotasController()
    
    def exibir(self):
        self._limpar_tela()
        self._exibir_cabecalho()
        
        alunos = self.controller.listar_alunos()
        
        if not alunos:
            print("\n✗ Nenhum aluno cadastrado!")
            input("[Pressione ENTER para continuar]")
            return
        
        print("\nAlunos disponíveis:\n")
        for i, aluno in enumerate(alunos, 1):
            print(f"{i}. {aluno.nome} (Notas: {len(aluno.notas)}/2)")
        
        try:
            escolha = int(input("\nEscolha o número do aluno (0 para cancelar): "))
            
            if escolha == 0:
                return
            
            if escolha < 1 or escolha > len(alunos):
                print("\n✗ Opção inválida!")
                input("[Pressione ENTER para continuar]")
                return
            
            aluno_id = alunos[escolha - 1].id
            aluno = self.controller.obter_aluno(aluno_id)
            
            print(f"\nAluno selecionado: {aluno.nome}")
            print(f"Notas registradas: {len(aluno.notas)}/2")
            
            if len(aluno.notas) >= 2:
                print("\n✗ Este aluno já possui 2 notas!")
                input("[Pressione ENTER para continuar]")
                return
            
            try:
                valor = float(input("\nDigite a nota (0-10): "))
                sucesso, mensagem = self.controller.lancar_nota(aluno_id, valor)
                
                if sucesso:
                    print(f"\n✓ {mensagem}")
                else:
                    print(f"\n✗ {mensagem}")
                
            except ValueError:
                print("\n✗ Digite um número válido!")
            
        except ValueError:
            print("\n✗ Entrada inválida!")
        
        input("\n[Pressione ENTER para continuar]")
    
    def _limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def _exibir_cabecalho(self):
        print("=" * 60)
        print(" " * 20 + "LANÇAR NOTAS")
        print("=" * 60)
