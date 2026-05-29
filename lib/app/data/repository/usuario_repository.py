from ..models import Usuario
from ..provider import UsuarioProvider


class UsuarioRepository:
    def __init__(self):
        self.provider = UsuarioProvider()
    
    def autenticar(self, username: str, password: str) -> bool:
        return self.provider.validar_login(username, password)
