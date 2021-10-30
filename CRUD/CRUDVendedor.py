from mysql.connector import Error
import Connection

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
            cursor.execute(sql)
            for i in cursor:
                print(i)

            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed select values: {}".format(err))

#Crud_vendedores.add_vendedor('16473198643',200,'2020-05-25','2020-05-26')
#Crud_vendedores.update_vendedor('16473198643',250,None)
#Crud_vendedores.select_vendedores()