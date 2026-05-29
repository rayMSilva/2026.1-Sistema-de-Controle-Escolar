import os
from ...controller.documento_controller import DocumentoController


class Documento:
    def __init__(self):
        self.controller = DocumentoController()
    
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
            print(f"{i}. {aluno.nome} (ID: {aluno.id})")
        
        try:
            escolha = int(input("\nEscolha o número do aluno (0 para cancelar): "))
            
            if escolha == 0:
                return
            
            if escolha < 1 or escolha > len(alunos):
                print("\n✗ Opção inválida!")
                input("[Pressione ENTER para continuar]")
                return
            
            aluno_id = alunos[escolha - 1].id
            aluno, msg = self.controller.obter_boletim(aluno_id)
            
            if aluno:
                self._exibir_boletim(aluno)
            else:
                print(f"\n✗ {msg}")
            
        except ValueError:
            print("\n✗ Entrada inválida!")
        
        input("\n[Pressione ENTER para continuar]")
    
    def _limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def _exibir_cabecalho(self):
        print("=" * 60)
        print(" " * 20 + "BOLETIM DE NOTAS")
        print("=" * 60)
    
    def _exibir_boletim(self, aluno):
        self._limpar_tela()
        
        print("=" * 60)
        print(" " * 20 + "BOLETIM ESCOLAR")
        print("=" * 60)
        
        print(f"\nAluno: {aluno.nome}")
        print(f"Matrícula: {aluno.matricula}")
        print(f"ID: {aluno.id}")
        
        print("\n" + "-" * 60)
        print("NOTAS:")
        print("-" * 60)
        
        if len(aluno.notas) == 0:
            print("\n✗ Nenhuma nota registrada ainda.")
        else:
            for i, nota in enumerate(aluno.notas, 1):
                print(f"Nota {i}: {nota:.1f}")
        
        print("\n" + "-" * 60)
        print("RESULTADO FINAL:")
        print("-" * 60)
        
        print(f"Média: {aluno.media:.2f}" if aluno.media > 0 else "Média: ---")
        print(f"Status: {aluno.obter_status()}")
        print("-" * 60)
