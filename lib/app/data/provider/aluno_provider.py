from ..models import Aluno
from ..sql.conexao_sql import ConexaoDB


class AlunoProvider:
    
    def __init__(self):
        self.db = ConexaoDB()
    
    def criar_aluno(self, nome: str, email: str) -> Aluno:
        sql = "SELECT MAX(id) as max_id FROM alunos"
        resultado = self.db.consultar_um(sql)
        proxima_matricula = (resultado['max_id'] + 1) if resultado['max_id'] else 1
        
        sql = """
            INSERT INTO alunos (nome, email, matricula)
            VALUES (?, ?, ?)
        """
        
        if self.db.executar(sql, (nome, email, proxima_matricula)):
            aluno_id = self.db.obter_ultimo_id()
            return Aluno(aluno_id, nome, email, proxima_matricula)
        
        return None
    
    def obter_aluno(self, aluno_id: int) -> Aluno:
        sql = "SELECT id, nome, email, matricula FROM alunos WHERE id = ?"
        resultado = self.db.consultar_um(sql, (aluno_id,))
        
        if resultado:
            aluno = Aluno(
                resultado['id'],
                resultado['nome'],
                resultado['email'],
                resultado['matricula']
            )
            aluno.notas = self._obter_notas_aluno(resultado['id'])
            aluno.calcular_media()
            return aluno
        return None
    
    def obter_aluno_por_email(self, email: str) -> Aluno:
        sql = "SELECT id, nome, email, matricula FROM alunos WHERE email = ?"
        resultado = self.db.consultar_um(sql, (email,))
        
        if resultado:
            return Aluno(
                resultado['id'],
                resultado['nome'],
                resultado['email'],
                resultado['matricula']
            )
        return None
    
    def obter_todos(self) -> list:
        sql = "SELECT id, nome, email, matricula FROM alunos ORDER BY nome"
        resultados = self.db.consultar_muitos(sql)
        
        alunos = []
        for resultado in resultados:
            aluno = Aluno(
                resultado['id'],
                resultado['nome'],
                resultado['email'],
                resultado['matricula']
            )
            aluno.notas = self._obter_notas_aluno(resultado['id'])
            aluno.calcular_media()
            alunos.append(aluno)
        
        return alunos
    
    def buscar_por_nome(self, nome: str) -> list:
        sql = "SELECT id, nome, email, matricula FROM alunos WHERE nome LIKE ? ORDER BY nome"
        resultados = self.db.consultar_muitos(sql, (f"%{nome}%",))
        
        alunos = []
        for resultado in resultados:
            aluno = Aluno(
                resultado['id'],
                resultado['nome'],
                resultado['email'],
                resultado['matricula']
            )
            aluno.notas = self._obter_notas_aluno(resultado['id'])
            aluno.calcular_media()
            alunos.append(aluno)
        
        return alunos
    
    def email_existe(self, email: str) -> bool:
        sql = "SELECT COUNT(*) as count FROM alunos WHERE email = ?"
        resultado = self.db.consultar_um(sql, (email,))
        return resultado['count'] > 0 if resultado else False
    
    def adicionar_nota(self, aluno_id: int, valor: float) -> bool:
        sql = """
            INSERT INTO notas (codigo_aluno, valor)
            VALUES (?, ?)
        """
        return self.db.executar(sql, (aluno_id, valor))
    
    def _obter_notas_aluno(self, aluno_id: int) -> list:
        sql = "SELECT valor FROM notas WHERE codigo_aluno = ? ORDER BY data_lancamento"
        resultados = self.db.consultar_muitos(sql, (aluno_id,))
        return [r['valor'] for r in resultados]
    
    def deletar_aluno(self, aluno_id: int) -> bool:
        sql = "DELETE FROM alunos WHERE id = ?"
        return self.db.executar(sql, (aluno_id,))
    
    def contar_alunos(self) -> int:
        sql = "SELECT COUNT(*) as total FROM alunos"
        resultado = self.db.consultar_um(sql)
        return resultado['total'] if resultado else 0
    
    def atualizar_aluno(self, aluno: Aluno) -> bool:
        sql = "UPDATE alunos SET nome = ? WHERE id = ?"
        return self.db.executar(sql, (aluno.nome, aluno.id))
