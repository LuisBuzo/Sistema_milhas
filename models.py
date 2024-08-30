import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='123456',
                database='viagens'
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexão ao MySQL foi encerrada")

class Passageiro:
    def __init__(self, nome, cpf, milhas):
        self.nome = nome
        self.cpf = cpf
        self.milhas = milhas

class Viagem:
    def __init__(self, companhia_aerea, local_saida, local_chegada):
        self.companhia_aerea = companhia_aerea
        self.local_saida = local_saida
        self.local_chegada = local_chegada
        self.passageiros = []

    def adicionar_passageiro(self, passageiro):
        self.passageiros.append(passageiro)
