import os
from ...controller.remover_aluno_controller import RemoverAlunoController


class RemoverAluno:
    def __init__(self):
        self.controller = RemoverAlunoController()
    
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
            print(f"{i}. {aluno.nome}")
        
        try:
            escolha = int(input("\nEscolha o número do aluno a remover (0 para cancelar): "))
            
            if escolha == 0:
                return
            
            if escolha < 1 or escolha > len(alunos):
                print("\n✗ Opção inválida!")
                input("[Pressione ENTER para continuar]")
                return
            
            aluno_id = alunos[escolha - 1].id
            aluno = self.controller.obter_aluno(aluno_id)
            
            print(f"\n⚠ Tem certeza que deseja remover '{aluno.nome}'?")
            confirmacao = input("Digite 'sim' para confirmar: ").strip().lower()
            
            if confirmacao == 'sim':
                if self.controller.remover_aluno(aluno_id):
                    print(f"\n✓ Aluno '{aluno.nome}' removido com sucesso!")
                else:
                    print("\n✗ Erro ao remover aluno!")
            else:
                print("\n✗ Remoção cancelada.")
            
        except ValueError:
            print("\n✗ Entrada inválida!")
        
        input("\n[Pressione ENTER para continuar]")
    
    def _limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def _exibir_cabecalho(self):
        print("=" * 60)
        print(" " * 20 + "REMOVER ALUNO")
        print("=" * 60)
