import sqlite3
import os

#classe dao, carrega os dados do usuario sqlite
class dbDao:

    #cria BD sqlite
    def createDb():
        conn = sqlite3.connect('daoUser.db')
        cursor = conn.cursor()
        sql ="CREATE TABLE user ("\
                "id INTEGER NOT NULL PRIMARY KEY,"\
                "userName varchar(50),"\
                "nomeCompleto varchar(50),"\
                "email varchar(50),"\
                "senha varchar(45),"\
                "fone varchar(15),"\
                "nomeBanco varchar(45));"

        cursor.execute(sql)
        cursor.close()
        conn.close()

    #insere os dados
    def insert(id,userName,nome,email,fone,senha,nomeBanco):
        dbDao.createDb()
        conn = sqlite3.connect('daoUser.db')
        cursor = conn.cursor()
        dados = (id,userName,nome,email,senha,fone,nomeBanco)
        sql = 'insert into user (id,userName,nomeCompleto,email,senha,fone, nomeBanco) values (?,?,?,?,?,?,?)'
        cursor.execute(sql,dados)
        conn.commit()
        cursor.close()
        conn.close()

    #atualiza os dados
    def update(id,nome,email,fone,senha):
        conn = sqlite3.connect('daoUser.db')
        cursor = conn.cursor()
        dados = (nome,email,fone,senha)
        sql = 'update user set nomeCompleto = %s, email = %s, fone = %s, senha = %s where id = '+id
        cursor.execute(sql,dados)
        conn.commit()
        cursor.close()
        conn.close()

    #seleciona os daods
    def select():
        conn = sqlite3.connect('daoUser.db')
        cursor = conn.cursor()
        sql = 'select * from user'
        cursor.execute(sql)
        result = []
        for i in cursor:
            result.append(i)
        cursor.close()
        conn.close()
        return [str(result[0][0]),result]

    #recupera o nome do banco
    def nomeBanco():
        conn = sqlite3.connect('daoUser.db')
        cursor = conn.cursor()
        sql = 'select nomeBanco from user'
        cursor.execute(sql)
        a = cursor.fetchone()
        cursor.close()
        conn.close()
        return(a[0])

    #exclui o arquivo
    def exclui():
        file = 'daoUser.db'
        os.remove(file)