import mysql.connector

class Aluno:
    def __init__(self, nome, contato, email):
        self.nome = nome
        self.contato = contato
        self.email = email

class Professor:
    def __init__(self, nome, contato, email):
        self.nome = nome
        self.contato = contato
        self.email = email

class Disciplina:
    def __init__(self, nome, carga_horaria):
        self.nome = nome
        self.carga_horaria = carga_horaria

class SistemaEscola:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="he182555@",
            database="escola"
        )
        self.cursor = self.conexao.cursor()

    def adicionar_aluno(self, aluno):
        sql = "INSERT INTO aluno (nome, contato, email) VALUES (%s, %s, %s)"
        valores = (aluno.nome, aluno.contato, aluno.email)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print('Aluno adicionado com sucesso.')

    def adicionar_professor(self, professor):
        sql = "INSERT INTO professor (nome, contato, email) VALUES (%s, %s, %s)"
        valores = (professor.nome, professor.contato, professor.email)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print('Professor adicionado com sucesso.')

    def adicionar_disciplina(self, disciplina):
        sql = "INSERT INTO disciplina (nome, carga_horaria) VALUES (%s, %s)"
        valores = (disciplina.nome, disciplina.carga_horaria)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print('Disciplina adicionada com sucesso.')

    def listar_dados(self):
        sql = "SELECT * FROM aluno, professor, disciplina"
        self.cursor.execute(sql)
        dados = self.cursor.fetchall()
        for dado in dados:
            print(f"ID do Aluno: {dado[0]}, Nome do Aluno: {dado[1]}, Contato: {dado[2]}, Email: {dado[3]}")
            print(f"ID do Professor: {dado[4]}, Nome do Professor: {dado[5]}, Contato: {dado[6]}, Email: {dado[7]}")
            print(f"ID da Disciplina: {dado[8]}, Nome da Disciplina: {dado[9]}, Carga Horária: {dado[10]}")

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()

# Instancia o sistema da escola
sistema_escola = SistemaEscola()

# Cria aluno
aluno = Aluno('joao victor', '991566532', 'joaovictor51@gmail.com')

# Cria professor
professor = Professor('davi noberto', '991453299', 'davinoberto55@gmail.com')

# Cria disciplina
disciplina = Disciplina('matematica', '300h')

# Adiciona aluno
sistema_escola.adicionar_aluno(aluno)

# Adiciona professor
sistema_escola.adicionar_professor(professor)

# Adiciona disciplina
sistema_escola.adicionar_disciplina(disciplina)

# Lista dados
print("Lista de Dados:")
sistema_escola.listar_dados()

# Fecha sistema de conexão
sistema_escola.fechar_conexao()
