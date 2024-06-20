CREATE DATABASE escola;
USE escola;

CREATE TABLE aluno (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    email varchar (50) not null
);

INSERT INTO aluno (nome, idade, email) VALUES ('Lucas', '17', 'Lucasgomes12@gmail.com');
INSERT INTO aluno (nome, idade, email) VALUES ('Maria', '19', 'Mariasilva34@gmail.com');

SELECT nome, idade, email FROM aluno;