import mysql.connector
import csv

class config:

    def conectar(self):
        self.conexao = mysql.connector.Connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'data',
        )
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        self.cursor.close()
        self.conexao.close()

    def query(self, sql, params = None):
        self.cursor.execute(sql, params or ())
        return self.cursor.fetchall()
    
    def inserir(self, nome):
        self.conectar()
        comando = f'INSERT INTO pessoa (nome) VALUES ("{nome}")'
        self.cursor.execute(comando)
        self.conexao.commit()
        print(f'\ninserido na tabela')
        self.desconectar()
    
    def inserircsv(self, nomedoarquivo):
        self.conectar()
        try:
            data = csv.DictReader(open(nomedoarquivo, encoding='utf-8'))
            for row in data:
                self.inserir(row['nome'])
                print('registro inserido')
        except Exception as erro:
            print('erro ao inserir csv', erro)
        self.desconectar()
    
    def deletar(self, id):
        self.conectar()
        try:
            comando = f'SELECT * FROM pessoa WHERE id = {id}'
            if not self.query(comando):
                return "registro não encontrado apra deletar"
            comando = f'DELETE FROM pessoa WHERE id = {id}'
            self.cursor.execute(comando)
            self.conexao.commit()
            print("registro deletado")     
        except Exception as erro:
            print('erro ao deletar', erro)
            print(f'\ninserido na tabela')
        self.desconectar()
    
    def atualizar(self, id, *args):
        self.conectar()
        try:
            comando = f'UPDATE pessoa SET nome = %s WHERE id = {id}'
            self.cursor.execute(comando, args)
            self.conexao.commit()
            print('Registro atualizado')
        except Exception as erro:
            print('Erro ao atualizar', erro)
        self.desconectar()
        

conf = config()

conf.inserircsv("data.csv")
conf.atualizar(1, 'Maria Antônio')
conf.deletar(2)