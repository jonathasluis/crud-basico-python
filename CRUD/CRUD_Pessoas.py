from mysql.connector import Error
import Connection

#classe clientes
class CrudPessoa:

    #insere um novo cliente
    def add_Pessoa(nome,cpf,sexo,estado,cidade,bairro,rua,numeroCasa,complemento,tipo):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = 'call addPessoa(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            dados = (nome,cpf,sexo,estado,cidade,bairro,rua,numeroCasa,complemento,tipo)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed insert values: {}".format(err))

    #atualiza dados de um cliente
    def update_Pessoa(cpf,nome,estado,cidade,bairro,rua,numeroCasa,complemento,tipo):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = 'call updPessoa(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            dados = (cpf,nome,estado,cidade,bairro,rua,numeroCasa,complemento,tipo)
            cursor.execute(sql,dados)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed update values: {}".format(err))

    #deleta todos os dados de um cliente
    def delete_Pessoa(cpf):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            sql = 'call delPessoa('+cpf+')'
            cursor.execute(sql)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed delete values: {}".format(err)) 

    #seleciona todos os clientes
    def select_Pessoa():
        cnx,cursor = Connection.Con.fazConexao()
        try:
            sql = 'SELECT * FROM Pessoa'
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


#CrudPessoa.add_Pessoa('jose','14725836982','m','ro','ro','centro','qq','4',None,'c')
#CrudPessoa.update_Pessoa('14725836982','hz','ro','ro','centro','qq','4',None,'c')
#CrudPessoa.delete_Pessoa('14725836982')
#CrudPessoa.select_Pessoa()