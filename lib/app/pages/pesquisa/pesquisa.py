import os

from ...controller.pesquisa_aluno_controller import PesquisaAlunoController


class Pesquisa:
    
    def __init__(self):
        self.controller = PesquisaAlunoController()
    
    def exibir(self):
        self._limpar_tela()
        self._exibir_cabecalho()
        
        nome = input("\nDigite o nome do aluno a buscar: ").strip()
        
        if not nome:
            print("\n✗ Busca cancelada.")
            input("[Pressione ENTER para continuar]")
            return
        
        alunos = self.controller.buscar_por_nome(nome)
        
        if not alunos:
            print(f"\n✗ Nenhum aluno encontrado com nome '{nome}'")
        else:
            print(f"\n✓ Encontrado(s) {len(alunos)} resultado(s):\n")
            self._exibir_tabela(alunos)
        
        input("\n[Pressione ENTER para continuar]")
    
    def _limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def _exibir_cabecalho(self):
        print("=" * 80)
        print(" " * 30 + "BUSCAR ALUNO")
        print("=" * 80)
    
    def _exibir_tabela(self, alunos: list):
        print("{:<5} {:<25} {:<15} {:<10} {:<15}".format(
            "ID", "Nome", "Matrícula", "Média", "Status"
        ))
        print("-" * 80) 
        
        for aluno in alunos:
            print("{:<5} {:<25} {:<15} {:<10} {:<15}".format(
                aluno.id,
                aluno.nome[:24],
                aluno.matricula,
                f"{aluno.media:.2f}" if aluno.media > 0 else "---",
                aluno.obter_status()
            ))
        
        print("-" * 80)
