import os

from ...controller.listar_alunos_controller import ListarAlunosController


class Listar:
    def __init__(self):
        self.controller = ListarAlunosController()
    
    def exibir(self):
        self._limpar_tela()
        self._exibir_cabecalho()
        
        alunos = self.controller.listar_todos()
        
        if not alunos:
            print("\n✗ Nenhum aluno cadastrado!")
        else:
            self._exibir_tabela(alunos)
        
        input("\n[Pressione ENTER para continuar]")
    
    def _limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def _exibir_cabecalho(self):
        print("=" * 80)
        print(" " * 30 + "LISTA DE ALUNOS")
        print("=" * 80)
    
    def _exibir_tabela(self, alunos: list):
        print("\n{:<5} {:<25} {:<15} {:<10} {:<15}".format(
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
        print(f"\nTotal: {len(alunos)} aluno(s) cadastrado(s)")
