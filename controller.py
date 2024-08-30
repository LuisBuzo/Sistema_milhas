from models import Database 
from models import Viagem
from mysql.connector import Error

class Controller:
    def __init__(self):
        self.db = Database()

    def cadastrar_passageiro(self, nome, cpf, milhas):
        try:
            if self.db.connection.is_connected():
                cursor = self.db.connection.cursor()
                sql_query = "INSERT INTO passageiros (nome, cpf, milhas) VALUES (%s, %s, %s)"
                valores = (nome, cpf, milhas)
                cursor.execute(sql_query, valores)
                self.db.connection.commit()
                print("Passageiro cadastrado com sucesso")
        except Error as e:
            print(f"Erro ao inserir passageiro: {e}")

    def comprar_viagem(self, cpf, id_viagem):
        try:
            if self.db.connection.is_connected():
                cursor = self.db.connection.cursor()
                cursor.execute("SELECT milhas FROM passageiros WHERE cpf = %s", (cpf,))
                milhas = cursor.fetchone()[0]

                cursor.execute("SELECT custo FROM viagens WHERE id = %s", (id_viagem,))
                custo_result = cursor.fetchone()
                if custo_result:
                    custo = custo_result[0]
                    if milhas >= custo:
                        cursor.execute("UPDATE passageiros SET milhas = milhas - %s WHERE cpf = %s", (custo, cpf))
                        cursor.execute("INSERT INTO passageiro_viagem (cpf, id_viagem) VALUES (%s, %s)", (cpf, id_viagem))
                        self.db.connection.commit()
                        print("Viagem comprada com sucesso")
                    else:
                        print("Milhas insuficientes")
                else:
                    print(f"Viagem com ID {id_viagem} não encontrada")
        except Error as e:
            print(f"Erro ao comprar viagem: {e}")

    def cadastrar_viagens_iniciais(self, id, companhia_aerea, local_saida, local_chegada, custo):
        try:
            if self.db.connection.is_connected():
                cursor = self.db.connection.cursor()
                sql_query = "INSERT INTO viagens (id, companhia_aerea, local_saida, local_chegada, custo) VALUES (%s, %s, %s, %s, %s)"
                valores = (id, companhia_aerea, local_saida, local_chegada, custo)
                cursor.execute(sql_query, valores)
                self.db.connection.commit()
                print("Viagem cadastrada com sucesso")
        except Error as e:
            print(f"Erro ao cadastrar viagens iniciais: {e}")
            
    def listar_passageiros(self, id_viagem):
        try:
            if self.db.connection.is_connected():
                cursor = self.db.connection.cursor()
                cursor.execute("""
                    SELECT p.nome, p.cpf
                    FROM passageiros p
                    JOIN passageiro_viagem pv ON p.cpf = pv.cpf
                    WHERE pv.id_viagem = %s
                """, (id_viagem,))
                return cursor.fetchall()
        except Error as e:
            print(f"Erro ao listar passageiros: {e}")
            return []
