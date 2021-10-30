from mysql.connector import Error
import Connection

#classe vendedor
class Crud_vendedores:

    #adiciona um vendedor
    def add_vendedor(id,salario,data_Admissao,data_Demissao):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = 'call addVendedor(%s,%s,%s,%s)'
            cursor.execute(sql)
            dados = (id,salario,data_Admissao,data_Demissao)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed insert values: {}".format(err))

    #atualiza dados de um vendedor
    def update_vendedor(db,id,nome,telefone,salario,data_demissao,estado,cidade,bairro,rua,numeroCasa,complemento):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            cursor.execute('USE '+db)
            sql = 'UPDATE `vendedores` SET `nome_vendedor` = %s,'\
                '`telefone_vendedor` = %s, `salario_vendedor` = %s,`data_demissao` = %s,'\
                '`estado_vendedor` = %s, `cidade_vendedor` = %s, `bairro_vendedor` = %s, `rua_vendedor` = %s,'\
                '`numeroCasa_vendedor` = %s, `complemento_vendedor` = %s WHERE `id_vendedor` = ' + str(id)
            dados = (nome,telefone,salario,data_demissao,estado,cidade,bairro,rua,numeroCasa,complemento)
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
