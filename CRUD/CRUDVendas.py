from mysql.connector import Error
from CRUD import Connection
import pandas as pd

#classe vendas
class Crud_vendas:

    #adiciona uma venda
    def add_venda(idProduto,cpfVendedor,cpfCliente,valor,qtd):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = 'call addVenda(%s,%s,%s,%s,%s)'
            dados = (idProduto,cpfCliente,cpfVendedor,valor,qtd)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed insert values: {}".format(err))

    #seleciona as vendas feitas
    def select_vendas():
        cnx,cursor = Connection.Con.fazConexao()
        try:
            sql = 'SELECT * FROM vendasjoin;'
            colunas = ['id produto','descição','cpf cliente','nome cliente','cpf vendedor',
                'nome vendedor','valor','quantidade']
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            df.columns = colunas
            df.set_index('id produto', inplace=True)
            print(df)
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed select values: {}".format(err))

#Crud_vendas.add_venda('3','14786474690','32478563248',500,1)
#Crud_vendas.select_vendas()