CREATE DATABASE e_commerce;
USE e_commerce;

CREATE TABLE produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(255) NOT NULL
);

INSERT INTO produto (nome, descricao) VALUES ('produto1', '25136546');
INSERT INTO produto (nome, descricao) VALUES ('produto2', '365151651');

SELECT nome, descricao FROM produto;