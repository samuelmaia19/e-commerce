import mysql.connector

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Produto:
    def __init__(self, nome, descricao, preco, estoque):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque

class Item:
    def __init__(self, quantidade, preco):
        self.quantidade = quantidade
        self.preco = preco

class SistemaECommerce:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="he182555@",
            database="e_commerce"
        )
        self.cursor = self.conexao.cursor()

    def adicionar_usuario(self, usuario):
        sql = "INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)"
        valores = (usuario.nome, usuario.email, usuario.senha)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print('Usuário adicionado com sucesso.')

    def adicionar_produto(self, produto):
        sql = "INSERT INTO produtos (nome, descricao, preco, estoque) VALUES (%s, %s, %s, %s)"
        valores = (produto.nome, produto.descricao, produto.preco, produto.estoque)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print('Produto adicionado com sucesso.')

    def adicionar_item(self, item):
        sql = "INSERT INTO itens (quantidade, preco) VALUES (%s, %s)"
        valores = (item.quantidade, item.preco)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print('Item adicionado com sucesso.')

    def listar_dados(self):
        sql = "SELECT * FROM usuario, produtos, itens"
        self.cursor.execute(sql)
        dados = self.cursor.fetchall()
        for dado in dados:
            print(f"ID do Usuário: {dado[0]}, Nome do Usuário: {dado[1]}, Email: {dado[2]}, Senha: {dado[3]}")
            print(f"ID do Produto: {dado[4]}, Nome do Produto: {dado[5]}, Descrição: {dado[6]}, Preço: {dado[7]}, Estoque: {dado[8]}")
            print(f"ID do Item: {dado[9]}, Quantidade: {dado[10]}, Preço do Item: {dado[11]}")

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()

# Instancia o sistema de e-commerce
sistema_ecommerce = SistemaECommerce()

# Cria usuário
usuario = Usuario('samuel', 'samuelmaia@gmail.com', 'samuelmaia19')

# Cria produto
produto = Produto('estencao', 'tem varias femeas', '$50,00', 'temos um estoque com 100')

# Cria item
item = Item('cem', 'cinquenta')

# Adiciona usuário
sistema_ecommerce.adicionar_usuario(usuario)

# Adiciona produto
sistema_ecommerce.adicionar_produto(produto)

# Adiciona item
sistema_ecommerce.adicionar_item(item)

# Lista dados
print("Lista de Dados:")
sistema_ecommerce.listar_dados()

# Fecha sistema de conexão
sistema_ecommerce.fechar_conexao()