from mysql.connector import Error
from CRUD import Connection
import pandas as pd

#classe vendedor
class Crud_vendedores:

    #adiciona um vendedor
    def add_vendedor(cpf,salario,data_Admissao,data_Demissao):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = 'call addVendedor(%s,%s,%s,%s);'
            dados = (cpf,salario,data_Admissao,data_Demissao)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed insert values: {}".format(err))

    #atualiza dados de um vendedor
    def update_vendedor(cpf,salario,data_demissao):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = 'call updvendedor(%s,%s,%s)'
            dados = (cpf,salario,data_demissao)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed update values: {}".format(err))

    #seleciona todas os vendedores
    def select_vendedores():
        cnx,cursor = Connection.Con.fazConexao()
        try:
            sql = 'SELECT * FROM vendedoresEstendido'
            colunas = ['cpf','nome','sexo','salario','data admissão','data demissão',
                'estado','cidade','bairro','rua','numero casa','complemento']
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            df.columns = colunas
            df.set_index('cpf', inplace=True)
            print(df)
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed select values: {}".format(err))