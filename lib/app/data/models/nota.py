class Nota:
    
    def __init__(self, id: int, codigo_aluno: int, valor: float):
        self.id = id
        self.codigo_aluno = codigo_aluno
        self.valor = valor if 0 <= valor <= 10 else 0.0
    
    def is_valida(self) -> bool:
        return 0 <= self.valor <= 10
    
    def __str__(self):
        return f"Nota: {self.valor:.1f}"
