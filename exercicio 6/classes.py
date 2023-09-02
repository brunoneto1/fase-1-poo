import mysql.connector


class bd:

    def conectar(self):
        self.conexao = mysql.connector.Connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'loja',
        )
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        self.cursor.close()
        self.conexao.close()

    def inserir(self, cod, prod):
        self.conectar()
        comando = f'INSERT INTO produto (codProduto, produto) VALUES ({cod}, "{prod}")'
        self.cursor.execute(comando)
        self.conexao.commit()
        print(f'\ninserido na tabela')
        self.desconectar()
