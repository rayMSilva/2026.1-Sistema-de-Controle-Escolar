import re


class Validador:
    
    @staticmethod
    def validar_nome(nome: str) -> tuple:
        if not nome:
            return False, "Nome não pode estar vazio"
        
        nome = nome.strip()
        
        if len(nome) < 3:
            return False, "Nome deve ter pelo menos 3 caracteres"
        
        if len(nome) > 100:
            return False, "Nome não pode exceder 100 caracteres"
        
        if not re.match(r"^[a-zA-ZáéíóúãõâêôçÁÉÍÓÚÃÕÂÊÔÇ\s]+$", nome):
            return False, "Nome deve conter apenas letras"
        
        return True, ""
    
    @staticmethod
    def validar_email(email: str) -> tuple:
        if not email:
            return False, "Email não pode estar vazio"
        
        email = email.strip()
        
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(padrao, email):
            return False, "Email inválido. Use o formato: usuario@dominio.com"
        
        return True, ""
