from mysql.connector import Error
import Connection as Conexao
from werkzeug import security
import usuario

#classe usuario
class Crud_usuario:

    #adiciona um novo usuario
    def addUser(userName,nomeCompleto,senha,email,telefone):
        cnx, cursor = Conexao.Con.fazConexao()
        try:
            cursor.execute("USE Usuarios")
            sql = "SELECT nome_user,email_user,telefone_user FROM usuarios"
            if Crud_usuario.verificaUser(cursor,userName,email,telefone,sql):
                sql = "INSERT INTO usuarios (nome_user, senha_user, email_user, telefone_user,nome_completo) VALUES (%s,%s,%s,%s,%s)"
                dados = (userName,security.generate_password_hash(senha),email,telefone,nomeCompleto)
                cursor.execute(sql,dados)
                cnx.commit()
                cursor.close()
                cnx.close()
                return True
        except Error as err:
            print("Failed insert values: {}".format(err))
            return False
    
    #atualiza os dados de um usuario
    def UpdateUser(nomeCompleto,senha,email,telefone,idUser):
        cnx, cursor = Conexao.Con.fazConexao()
        try:
            cursor.execute("USE Usuarios")
            sql = "SELECT nome_user, email_user,telefone_user FROM usuarios where id_usuario  != " + str(idUser)
            if Crud_usuario.verificaUser(cursor,'',email,telefone,sql):
                sql = "UPDATE usuarios SET email_user = %s, senha_user = %s, telefone_user = %s, nome_completo = %s"\
                    "WHERE id_usuario = " + idUser
                dados = (email,security.generate_password_hash(senha),telefone,nomeCompleto)
                cursor.execute(sql,dados)
                cnx.commit()
                cursor.close()
                cnx.close()
                usuario.dbDao.update(idUser,nomeCompleto,email,telefone,senha)
        except Error as err:
            print("Failed update values: {}".format(err))

    #atualiza a senha de um usuario
    def UpdateSenhaUser(senha,user):
        cnx, cursor = Conexao.Con.fazConexao()
        try:
            cursor.execute("USE Usuarios")
            cursor.execute('SELECT id_usuario FROM Usuarios.usuarios where email_user = \''+user+'\'')
            id = cursor.fetchone()[0]
            has = (security.generate_password_hash(senha))
            sql = 'UPDATE usuarios SET senha_user = \''+has +'\' WHERE id_usuario = ' + str(id)
            cursor.execute(sql)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed update values: {}".format(err))

    #deleta um usuario
    def DeleteUser(idUser):
        cnx, cursor = Conexao.Con.fazConexao()
        try:
            cursor.execute("USE Usuarios")
            sql = "DELETE FROM usuarios where id_usuario  = " + str(idUser)
            cursor.execute(sql)
            cnx.commit()
            cursor.close()
            cnx.close()
        except Error as err:
            print("Failed remove values: {}".format(err))

    #verifica se ja existe o usuario
    def verificaUser(cursor,userName,email,telefone,sql):
        cursor.execute("USE Usuarios")
        cursor.execute(sql)

        for c_nome,c_email,c_telefone in cursor:
            if c_nome == userName and c_email == email and c_telefone == telefone:
                print("usuario ja cadastrado")
                cursor.close()
                return False
            elif c_nome == userName:
                print('ja existe um usuario com esse username')
                cursor.close()
                return False
            elif c_email == email:
                print('ja existe um usuario com esse email')
                cursor.close()
                return False
            elif c_telefone == telefone:
                print('ja existe um usuario com esse telefone')
                cursor.close()
                return False
        
        return True

