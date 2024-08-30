CREATE DATABASE viagens;

USE viagens;

CREATE TABLE passageiros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    milhas INT NOT NULL
);

CREATE TABLE viagens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    companhia_aerea VARCHAR(255) NOT NULL,
    local_saida VARCHAR(255) NOT NULL,
    local_chegada VARCHAR(255) NOT NULL,
    custo INT NOT NULL
);

CREATE TABLE passageiro_viagem (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(14),
    id_viagem INT,
    FOREIGN KEY (cpf) REFERENCES passageiros(cpf),
    FOREIGN KEY (id_viagem) REFERENCES viagens(id)
);
