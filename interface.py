from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from controller import Controller

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_window.ui", self)  # Carrega o arquivo .ui na janela principal

        self.controller = Controller()

        
         
        # Conectar os sinais aos slots (funções)
        self.btnCadastrarPassageiro.clicked.connect(self.cadastrar_passageiro)
        self.btnComprarViagem.clicked.connect(self.comprar_viagem)
        self.btnCadastrarViagem.clicked.connect(self.cadastrar_viagens_iniciais)
        self.btnListar.clicked.connect(self.listar_passageiros)

    def cadastrar_passageiro(self):
        print("Debug: Clicou em cadastrar passageiro")  # Debug
        nome = self.inputNome.text()
        cpf = self.inputCpf.text()
        milhas = int(self.inputMilhas.text())
        self.controller.cadastrar_passageiro(nome, cpf, milhas)
        self.output_message(f"Passageiro '{nome}' cadastrado com sucesso")

    def cadastrar_viagens_iniciais(self):
        print("Debug: Clicou em cadastrar viagem")  # Debug
        id = self.inputIdCadastro.text()
        companhia_aerea = self.inputCompanhia.text()
        local_saida = self.inputOrigem.text()
        local_chegada = self.inputDestino.text()
        custo = int(self.inputCusto.text())
        self.controller.cadastrar_viagens_iniciais(id, companhia_aerea, local_saida, local_chegada, custo)
        self.output_message(f"Viagem '{id}' cadastrado com sucesso")
    
    def listar_passageiros(self):
        id_viagem_text = self.inputIdConsulta.text()

        # Verifica se o campo de id_viagem não está vazio
        if id_viagem_text.strip():  # verifica se há texto não vazio
            try:
                id_viagem = int(id_viagem_text)
                passageiros = self.controller.listar_passageiros(id_viagem)
                if passageiros:
                    for passageiro in passageiros:
                        nome, cpf = passageiro
                        self.output_message(f"Nome: {nome}, CPF: {cpf}")
                else:
                    self.output_message("Nenhum passageiro encontrado para esta viagem")
            except ValueError:
                self.output_message("ID da viagem deve ser um número inteiro válido")
        else:
            self.output_message("Por favor, insira o ID da viagem")
        
    def comprar_viagem(self):
        cpf = self.inputCpfCompra.text()
        id_viagem_text = self.inputIdViagem.text()

        # Verifica se o campo de id_viagem não está vazio
        if id_viagem_text.strip():  # verifica se há texto não vazio
            try:
                id_viagem = int(id_viagem_text)
                self.controller.comprar_viagem(cpf, id_viagem)
                self.output_message(f"Viagem ID {id_viagem} comprada para CPF {cpf}")
            except ValueError:
                self.output_message("ID da viagem deve ser um número inteiro válido")
        else:
            self.output_message("Por favor, insira o ID da viagem")

    def output_message(self, message):
        print(f"Debug: Exibindo mensagem: {message}")  
        current_text = self.txtOutput.toPlainText()
        if current_text:
            current_text += "\n"
        self.txtOutput.setPlainText(current_text + message)
        QtWidgets.QApplication.processEvents()  # Força a atualização da interface
    
   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
