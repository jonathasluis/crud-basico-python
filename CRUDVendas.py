from mysql.connector import Error
from CRUDProdutos import Crud_Produtos
import Connection

#classe vendas
class Crud_vendas:

    #adiciona uma venda
    def add_venda(db,idProduto,idVendedor,idCliente,valor,qtd):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            cursor.execute('USE '+db)
            sql = 'INSERT INTO `vendas` (`id_produto`, `id_vendedor`, `id_cliente`, `valor`,`quantidade`)'\
                'VALUES (%s, %s, %s, %s,%s);'
            dados = (idProduto,idVendedor,idCliente,valor,qtd)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
            Crud_Produtos.UpdateQTD_Produto(db,idProduto,qtd)
        except Error as err:
            print("Failed insert values: {}".format(err))

    #seleciona as vendas feitas
    def select_vendas(db):
        cnx,cursor = Connection.Con.fazConexao()
        try:
            cursor.execute("USE "+db)
            sql = 'select v.id_venda, p.descricao as \'descricao do produto\', c.nome_cliente as \'cliente\','\
                'a.nome_vendedor as \'vendedor\',v.valor,v.quantidade from vendas as v '\
                'left join produtos as p on v.id_produto  = p.id_produto '\
                'left join clientes as c on  v.id_cliente = c.id_cliente '\
                'left join vendedores as a on v.id_vendedor = a.id_vendedor;'
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