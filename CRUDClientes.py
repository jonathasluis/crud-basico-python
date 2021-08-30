from mysql.connector import Error
import Connection

#classe clientes
class Crud_clientes:

    #insere um novo cliente
    def add_cliente(db,nome,cpf,telefone,estado,cidade,bairro,rua,numeroCasa,complemento):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            cursor.execute('USE '+db)
            sql = 'SELECT * FROM clientes WHERE cpf_cliente = '+ str(cpf)
            cursor.execute(sql)
            result = cursor.fetchone()
            if result == None:
                sql = ' INSERT INTO `clientes` (`nome_cliente`, `cpf_cliente`,`telefone_cliente`,'\
                    '`estado_clente`, `cidade_cliente`, `bairro_cliente`,`rua_cliente`, `numeroCasa_cliente`,'\
                    '`complemento_cliente`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
                dados = (nome,cpf,telefone,estado,cidade,bairro,rua,numeroCasa,complemento)
                cursor.execute(sql,dados)
                cnx.commit()
                cursor.close()
                cnx.close()
            else:
                print('ja existe um cliente com esse cpf cadastrado: '+ str(result[1:4]))
        except Error as err:
            print("Failed insert values: {}".format(err))

    #atualiza dados de um cliente
    def update_cliente(db,id,nome,telefone,estado,cidade,bairro,rua,numeroCasa,complemento):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            cursor.execute('USE '+db)
            sql = 'UPDATE `clientes` SET `nome_cliente` = %s, `telefone_cliente` = %s,'\
                '`estado_clente` = %s, `cidade_cliente` = %s, `bairro_cliente` = %s, `rua_cliente` = %s,'\
                '`numeroCasa_cliente` = %s, `complemento_cliente` = %s WHERE `id_cliente` = ' + str(id)
            dados = (nome,telefone,estado,cidade,bairro,rua,numeroCasa,complemento)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed update values: {}".format(err))

    #deleta todos os dados de um cliente
    def delete_cliente(db,id):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            cursor.execute('USE '+db)
            sql =  'DELETE FROM `clientes` WHERE `id_cliente` = ' + str(id)
            cursor.execute(sql)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed delete values: {}".format(err)) 

    #seleciona todos os clientes
    def select_clientes(db):
        cnx,cursor = Connection.Con.fazConexao()
        try:
            cursor.execute("USE "+db)
            sql = 'SELECT * FROM clientes'
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