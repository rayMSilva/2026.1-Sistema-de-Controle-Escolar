class Aluno:
    def __init__(self, id: int, nome: str, email: str, matricula: int = None):
        self.id = id
        self.nome = nome
        self.email = email
        self.matricula = matricula if matricula is not None else id
        self.notas = []
        self.media = 0.0
    
    def adicionar_nota(self, valor: float) -> bool:
        if len(self.notas) < 2:
            if 0 <= valor <= 10:
                self.notas.append(valor)
                self.calcular_media()
                return True
        return False
    
    def calcular_media(self) -> float:
        if len(self.notas) >= 2:
            self.media = sum(self.notas) / len(self.notas)
        else:
            self.media = 0.0
        return round(self.media, 2)
    
    def obter_status(self) -> str:
        if self.media >= 7:
            return "Aprovado"
        elif self.media >= 5:
            return "Recuperação"
        elif len(self.notas) < 2:
            return "Cursando"
        else:
            return "Reprovado"
    
    def __str__(self):
        return f"{self.nome} - Matrícula: {self.matricula} - Média: {self.media:.2f} ({self.obter_status()})"
