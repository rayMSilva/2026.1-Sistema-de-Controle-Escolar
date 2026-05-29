import sqlite3
import os
from pathlib import Path


class ConexaoDB:
    
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ConexaoDB, cls).__new__(cls)
            cls._instancia._inicializar()
        return cls._instancia
    
    def _inicializar(self):
        self.caminho_db = Path.home() / ".escolar" / "escolar.db"
        self.caminho_db.parent.mkdir(parents=True, exist_ok=True)
        
        self.conexao = sqlite3.connect(str(self.caminho_db))
        self.conexao.row_factory = sqlite3.Row
        self.conexao.execute("PRAGMA foreign_keys = ON")
        
        self._criar_tabelas()
    
    def _criar_tabelas(self):
        cursor = self.conexao.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                matricula INTEGER NOT NULL UNIQUE,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo_aluno INTEGER NOT NULL,
                valor REAL NOT NULL CHECK(valor >= 0 AND valor <= 10),
                data_lancamento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (codigo_aluno) REFERENCES alunos(id) ON DELETE CASCADE
            )
        """)
        
        cursor.execute("SELECT COUNT(*) FROM usuarios WHERE username = 'admin'")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO usuarios (username, password) VALUES ('admin', 'admin')")
        
        self.conexao.commit()
    
    def executar(self, sql: str, parametros: tuple = None) -> bool:
        try:
            cursor = self.conexao.cursor()
            if parametros:
                cursor.execute(sql, parametros)
            else:
                cursor.execute(sql)
            self.conexao.commit()
            return True
        except sqlite3.IntegrityError as e:
            self.conexao.rollback()
            print(f"Erro de integridade: {e}")
            return False
        except Exception as e:
            self.conexao.rollback()
            print(f"Erro ao executar: {e}")
            return False
    
    def consultar_um(self, sql: str, parametros: tuple = None) -> dict:
        try:
            cursor = self.conexao.cursor()
            if parametros:
                cursor.execute(sql, parametros)
            else:
                cursor.execute(sql)
            resultado = cursor.fetchone()
            return dict(resultado) if resultado else None
        except Exception as e:
            print(f"Erro ao consultar: {e}")
            return None
    
    def consultar_muitos(self, sql: str, parametros: tuple = None) -> list:
        try:
            cursor = self.conexao.cursor()
            if parametros:
                cursor.execute(sql, parametros)
            else:
                cursor.execute(sql)
            resultados = cursor.fetchall()
            return [dict(r) for r in resultados]
        except Exception as e:
            print(f"Erro ao consultar: {e}")
            return []
    
    def obter_ultimo_id(self) -> int:
        try:
            cursor = self.conexao.cursor()
            return cursor.lastrowid
        except Exception as e:
            print(f"Erro ao obter ID: {e}")
            return None
    
    def fechar(self):
        if self.conexao:
            self.conexao.close()
    
    def __del__(self):
        self.fechar()
