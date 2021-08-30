import mysql.connector

class Con:

    def fazConexao():

        config = {
            'user': 'root',
            'password': 'root',
            'host': '192.168.0.200',
            'raise_on_warnings': True}

        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        return [cnx,cursor]

