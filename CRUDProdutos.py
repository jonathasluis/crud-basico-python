from mysql.connector import Error
import Connection

#classe produtos
class Crud_Produtos:

    #adiciona um novo produto
    def addProduto(db,id,descricao,marca,cor,tamanho,genero,categoria,qtd,precoCusto):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            cursor.execute("USE "+ db)
            sql = "SELECT * FROM produtos WHERE id_produto = " + str(id)
            if Crud_Produtos.verificaProduto(cursor,sql,db):
                sql= "INSERT INTO produtos (id_produto, descricao, marca, cor, tamanho, genero, categoria, quantidade, preco_custo)"\
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                dados = (id,descricao,marca,cor,tamanho,genero,categoria,qtd,precoCusto)
                cursor.execute(sql,dados)
                cnx.commit()
                cursor.close()
                cnx.close()
        except Error as err:
            print("Failed insert values: {}".format(err))

    #deleta um produto
    def deleteProduto(db,id):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            cursor.execute("USE "+db)
            sql = "DELETE FROM produtos where id_produto  = " + str(id)
            cursor.execute(sql)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed remove values: {}".format(err))

    #atualiza os dados de um produto
    def UpdateProduto(db,id,descricao,marca,cor,tamanho,genero,categoria,qtd,precoCusto):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            cursor.execute("USE "+ db)
            sql = "UPDATE produtos SET descricao = %s, marca = %s, cor = %s, tamanho = %s, genero = %s, categoria = %s, "\
                "quantidade = %s, preco_custo = %s WHERE id_produto = " + str(id)
            dados = (descricao,marca,cor,tamanho,genero,categoria,qtd,precoCusto)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed update values: {}".format(err))

    #atualiza a quantidade de um determinado produto
    def UpdateQTD_Produto(db,id,qtd):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            cursor.execute("USE "+ db)
            cursor.execute('SELECT quantidade FROM produtos WHERE id_produto = '+str(id))
            qtd_origem = int(cursor.fetchone()[0])
            nova_qtd = qtd_origem - int(qtd)
            sql = 'UPDATE `produtos` SET `quantidade` = %s WHERE `id_produto` = %s;'
            dados = (nova_qtd,id)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed update values: {}".format(err))

    #seleciona os produtos
    def selectProdutos(db):
        cnx,cursor = Connection.Con.fazConexao()
        try:
            cursor.execute("USE "+db)
            sql = 'SELECT id_produto, descricao, marca, cor, tamanho, genero, c.valor, quantidade, '\
                'preco_custo FROM produtos '\
                'left join categorias.tipos_subcategoria as c on categoria = c.id;'
            cursor.execute(sql)
            result = []
            for i in cursor:
                result.append(i)

            cursor.close()
            cnx.close()
            for i in result:
                print(i)
        except Error as err:
            print("Failed select values: {}".format(err))

    #verifica se ja existe um produto cadastrado
    def verificaProduto(cursor,sql,db):
        cursor.execute("USE "+ db)
        cursor.execute(sql)

        result = cursor.fetchone()
        if result == None:
            return True
        else:
            print('ja existe um produto com esse Codigo!')
            return False