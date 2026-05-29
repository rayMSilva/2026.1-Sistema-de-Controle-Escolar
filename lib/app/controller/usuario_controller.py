from ..data.repository import UsuarioRepository


class UsuarioController:
    
    def __init__(self):
        self.repository = UsuarioRepository()
    
    def autenticar(self, username: str, password: str) -> tuple:
        if not username or not password:
            return False, "Usuário e senha não podem estar vazios"
        
        if self.repository.autenticar(username, password):
            return True, f"Bem-vindo, {username}!"
        else:
            return False, "Usuário ou senha incorretos"
