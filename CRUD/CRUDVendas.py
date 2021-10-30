from mysql.connector import Error
import Connection

#classe vendas
class Crud_vendas:

    #adiciona uma venda
    def add_venda(idProduto,idVendedor,idCliente,valor,qtd):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = 'call addVenda(%s,%s,%s,%s,%s)'
            dados = (idProduto,idCliente,idVendedor,valor,qtd)
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
            cursor.execute(sql)
            for i in cursor:
                print(i)

            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed select values: {}".format(err))