from mysql.connector import Error
import Connection

#classe vendedor
class Crud_vendedores:

    #adiciona um vendedor
    def add_vendedor(db,nome,cpf,telefone,salario,data_Admissao,data_Demissao,estado,cidade,bairro,rua,numeroCasa,complemento):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            cursor.execute('USE '+db)
            sql = 'SELECT * FROM vendedores WHERE cpf_vendedor = '+ str(cpf)
            cursor.execute(sql)
            result = cursor.fetchone()
            if result == None:
                sql = 'INSERT INTO `vendedores` (`nome_vendedor`, `cpf_vendedor`, `telefone_vendedor`,'\
                    '`salario_vendedor`, `data_admissao`, `data_demissao`, `estado_vendedor`, `cidade_vendedor`, `bairro_vendedor`,'\
                    '`rua_vendedor`, `numeroCasa_vendedor`, `complemento_vendedor`)'\
                    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)'
                dados = (nome,cpf,telefone,salario,data_Admissao,data_Demissao,estado,cidade,bairro,rua,numeroCasa,complemento)
                cursor.execute(sql,dados)
                cnx.commit()
                cursor.close()
                cnx.close()
            else:
                print('ja existe um vendedor com esse cpf cadastrado: '+ str(result[1:4]))
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

    #deleta o registro de um vendedor
    def delete_vendedor(db,id):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            cursor.execute('USE '+db)
            sql =  'DELETE FROM `vendedores` WHERE `id_vendedor` = ' + str(id)
            cursor.execute(sql)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed delete values: {}".format(err)) 

    #seleciona todas os vendedores
    def select_vendedores(db):
        cnx,cursor = Connection.Con.fazConexao()
        try:
            cursor.execute("USE "+db)
            sql = 'SELECT * FROM vendedores'
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