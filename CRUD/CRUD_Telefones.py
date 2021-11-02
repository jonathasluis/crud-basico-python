from mysql.connector import Error
from CRUD import Connection
import pandas as pd

#classe telefones
class CrudTelefones:

    #insere um novo telefone
    def insert_Telefone(cpf,numero):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = 'call addtelefone(%s,%s)'
            dados = (cpf,numero)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed insert values: {}".format(err))

    #atualiza dados de um telefone
    def update_Telefone(cpf,numeroNovo,telefoneAntigo):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = 'call updTelefone(%s,%s,%s)'
            dados = (cpf,numeroNovo,telefoneAntigo)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed update values: {}".format(err))

    #deleta todos os dados de um telefone
    def delete_Telefone(cpf,numero):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = 'call delTelefone(%s,%s)'
            dados = (cpf,numero)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed delete values: {}".format(err)) 

    #seleciona todos os telefones de uma pessoa
    def select_Telefone(cpf):
        cnx,cursor = Connection.Con.fazConexao()
        try:
            sql = 'SELECT telefone FROM telefones WHERE cpf ='+ cpf
            colunas = ['telefone']
            cursor.execute(sql)
            data = cursor.fetchall()
            if data != []:
                df = pd.DataFrame(data)
                df.columns = colunas
                df.index = range(1, len(df)+1)
                print(df)
            else:
                print('não há telefones!')

            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed select values: {}".format(err))