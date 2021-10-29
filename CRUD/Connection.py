import mysql.connector
from mysql.connector import Error

class Con:

    def fazConexao():

        config = {
            'user': 'root',
            'password': 'root',
            'host': '127.0.0.1',
            'raise_on_warnings': True,
            'database': 'DB_Jonathas'}

        try:
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            return [cnx,cursor]
        except Error as err:
            print("Failed connect to database: {}".format(err))