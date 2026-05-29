class Usuario:
    def __init__(self, id: int = 1, username: str = "admin", password: str = "admin"):
        self.id = id
        self.username = username
        self.password = password
    
    def validar_credenciais(self, username: str, password: str) -> bool:
        return self.username == username and self.password == password
    
    def __str__(self):
        return f"Usuario: {self.username}"
