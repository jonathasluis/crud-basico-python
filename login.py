from CRUDUser import Crud_usuario
from mysql.connector import Error
import Connection as Connection
from werkzeug import security
import sendEmail
import random, string
import usuario as dao

#classe login
class Login:

    #faz o login do usuario, verifica se o nome ou email estao no banco
    def logar(nome,senha):
        cnx, cursor = Connection.Con.fazConexao()
        try:
            cursor.execute("USE Usuarios")
            sql = "SELECT * FROM usuarios WHERE nome_user = %s or email_user = %s"
            cursor.execute(sql,(nome,nome))
            a = cursor.fetchone()
            
            if a == None:
                print("conta nao encontrada")
                cursor.close()
                cnx.close()
                return [False,0]
            else:
                if security.check_password_hash(a[2],senha):#verifica a hash da senha
                    print("logado")
                    nomeDb = Login.pegarDados(a[1])
                    dao.dbDao.insert(a[0],a[1],a[5],a[3],a[4],senha,nomeDb)
                    return [True,1]
                else:
                    print("senha incorreta")
                    cursor.close()
                    cnx.close()
                    return [False,1]

        except Error as err:
            print("Failed insert values: {}".format(err))

    #retorna o nome do banco do usuario
    def pegarDados(nome):
        nomeDB = 'DB_' + nome
        return nomeDB

    #envia um email de recuperaçao de senha
    def esqueceuSenha(email):
        userName = ''#email remetente
        password = ''#senha do email remetente
        assunto = 'Recuperação de senha'
        novaSenha = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        conteudo = 'sua senha de recuperação é: '+  novaSenha
        Crud_usuario.UpdateSenhaUser(novaSenha,email)
        sendEmail.sendEmail(userName,password,[email],assunto,conteudo)


#Login.logar('jonathassousasgs@gmail.com','Jonathas','123456')
#Login.esqueceuSenha('jonathassousasgs@gmail.com')