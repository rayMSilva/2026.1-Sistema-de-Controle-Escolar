import os
from .pages.saudacao.saudacao import Saudacao
from .pages.login.login import Login
from .pages.menu.menu import Menu
from .pages.cadastro_aluno.cadastro_aluno import CadastroAluno
from .pages.cadastro_notas.notas import NotasPage
from .pages.listar.listar import Listar
from .pages.pesquisa.pesquisa import Pesquisa
from .pages.documento.documento import Documento
from .pages.remover_aluno.remover_aluno import RemoverAluno


class App:
    
    def __init__(self):
        self.saudacao = Saudacao()
        self.login = Login()
        self.menu = Menu()
        self.cadastro = CadastroAluno()
        self.notas = NotasPage()
        self.listar = Listar()
        self.remover = RemoverAluno()
        self.pesquisa = Pesquisa()
        self.documento = Documento()
    
    def executar(self):
        try:
            if not self.saudacao.exibir():
                return
            if not self.login.exibir():
                return
            
            while True:
                opcao = self.menu.exibir()
                
                if opcao == '1':
                    self.cadastro.exibir()
                
                elif opcao == '2':
                    self.listar.exibir()
                
                elif opcao == '3':
                    self.notas.exibir()
                
                elif opcao == '4':
                    self.documento.exibir()
                
                elif opcao == '5':
                    self.pesquisa.exibir()
                
                elif opcao == '6':
                    self.remover.exibir()
                
                elif opcao == '7':
                    self._limpar_tela()
                    print("\nObrigado por usar o Sistema de Controle Escolar!")
                    print("Até logo!")
                    break
        
        except KeyboardInterrupt:
            self._limpar_tela()
            print("\n\nSistema encerrado. Até logo!")
    
    def _limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')