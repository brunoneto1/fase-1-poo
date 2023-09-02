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

    def listar(self):
        self.conectar()
        comando = f'SELECT * FROM produto'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        for r in resultado:
            print(f'{r[0]} | {r[1]}')
        self.desconectar()

comandos = bd()
comandos.listar()