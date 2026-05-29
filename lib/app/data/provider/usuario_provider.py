from ..sql.conexao_sql import ConexaoDB
from ..models import Usuario


class UsuarioProvider:
    def __init__(self):
        self.db = ConexaoDB()
        self.inserir_usuario(1, "admin", "admin")
    
    def validar_login(self, username, password):
        sql = "SELECT 1 FROM usuarios WHERE username = ? AND password = ?"
        resultado = self.db.consultar_um(sql, (username, password))
        return resultado is not None

    def inserir_usuario(self, id, username, password):
        sql = """
            INSERT INTO usuarios (id, username, password)
            VALUES (?, ?, ?)
        """
        
        if self.db.executar(sql, (id, username, password)):
            return Usuario(id, username, password)
        
        return None
