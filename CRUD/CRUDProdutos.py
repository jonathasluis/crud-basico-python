from mysql.connector import Error
import Connection

#classe produtos
class Crud_Produtos:

    #adiciona um novo produto
    def addProduto(id,descricao,marca,cor,tamanho,genero,categoria,qtd,precoCusto):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql= "call addProduto(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            dados = (id,descricao,marca,cor,tamanho,genero,categoria,qtd,precoCusto)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed insert values: {}".format(err))

    #deleta um produto
    def deleteProduto(id):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = "call delProduto(\'"+ id +"\')"
            cursor.execute(sql)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed remove values: {}".format(err))

    #atualiza os dados de um produto
    def UpdateProduto(id,descricao,marca,cor,tamanho,genero,categoria,qtd,precoCusto):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = "call updproduto(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            dados = (id,descricao,marca,cor,tamanho,genero,categoria,qtd,precoCusto)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed update values: {}".format(err))

    #seleciona os produtos
    def selectProdutos():
        cnx,cursor = Connection.Con.fazConexao()
        try:
            sql = 'SELECT * FROM produto_estendido'
            cursor.execute(sql)
            for i in cursor:
                print(i)
            cursor.close()
            cnx.close()
    
        except Error as err:
            print("Failed select values: {}".format(err))

