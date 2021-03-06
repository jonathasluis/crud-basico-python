from mysql.connector import Error
from CRUD import Connection
import pandas as pd

#classe clientes
class CrudPessoa:

    #insere um novo cliente
    def add_Pessoa(nome,cpf,sexo,estado,cidade,bairro,rua,numeroCasa,complemento,tipo):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = 'call addPessoa(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            dados = (nome,cpf,sexo,estado,cidade,bairro,rua,numeroCasa,complemento,tipo)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed insert values: {}".format(err))

    #atualiza dados de um cliente
    def update_Pessoa(cpf,nome,estado,cidade,bairro,rua,numeroCasa,complemento,tipo):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = 'call updPessoa(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            dados = (cpf,nome,estado,cidade,bairro,rua,numeroCasa,complemento,tipo)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed update values: {}".format(err))

    #deleta todos os dados de um cliente
    def delete_Pessoa(cpf):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = 'call delPessoa('+cpf+')'
            cursor.execute(sql)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed delete values: {}".format(err)) 

    #seleciona todos os clientes
    def select_Pessoa():
        cnx,cursor = Connection.Con.fazConexao()
        try:
            sql = 'SELECT * FROM Pessoa'
            colunas = ['cpf','nome','sexo','estado','cidade','bairro','rua','numero casa','complemento','tipo']
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            df.columns = colunas
            df.set_index('cpf', inplace=True)
            print(df)
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed select values: {}".format(err))