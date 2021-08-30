import mysql.connector
from mysql.connector import errorcode
import Connection as Conexao

#tabelas do banco de dados
tabelas = ["CREATE TABLE IF NOT EXISTS `produtos` ("\
    "`id_produto` BIGINT NOT NULL,"\
    "`descricao` VARCHAR(45),"\
    "`marca` VARCHAR(45),"\
    "`cor` VARCHAR(45),"\
    "`tamanho` VARCHAR(45),"\
    "`genero` VARCHAR(1),"\
    "`categoria` INT,"\
    "`quantidade` INT,"\
    "`preco_custo` FLOAT,"\
    "PRIMARY KEY (`id_produto`),"\
    "CONSTRAINT `categoria`"\
    "FOREIGN KEY (`categoria`)"\
    "REFERENCES `categorias`.`tipos_subcategoria` (`id`) "\
    "ON DELETE NO ACTION "\
    "ON UPDATE NO ACTION);",
    
    'CREATE TABLE IF NOT EXISTS `clientes` ('\
    '`id_cliente` INT NOT NULL AUTO_INCREMENT,'\
    '`nome_cliente` VARCHAR(45) NULL,'\
    '`cpf_cliente` VARCHAR(11) NULL,'\
    '`telefone_cliente` VARCHAR(15) NULL,'\
    '`estado_clente` VARCHAR(2) NULL,'\
    '`cidade_cliente` VARCHAR(50) NULL,'\
    '`bairro_cliente` VARCHAR(45) NULL,'\
    '`rua_cliente` VARCHAR(45) NULL,'\
    '`numeroCasa_cliente` VARCHAR(45) NULL,'\
    '`complemento_cliente` VARCHAR(10) NULL,'\
    'PRIMARY KEY (`id_cliente`));',

    'CREATE TABLE IF NOT EXISTS `vendedores` ('\
    '`id_vendedor` INT NOT NULL AUTO_INCREMENT,'\
    '`nome_vendedor` VARCHAR(45) NULL,'\
    '`cpf_vendedor` VARCHAR(11) NULL,'\
    '`telefone_vendedor` VARCHAR(15) NULL,'\
    '`salario_vendedor` FLOAT NULL,'\
    '`data_admissao` DATE NULL,'\
    '`data_demissao` DATE NULL,'\
    '`estado_vendedor` VARCHAR(2) NULL,'\
    '`cidade_vendedor` VARCHAR(45) NULL,'\
    '`bairro_vendedor` VARCHAR(45) NULL,'\
    '`rua_vendedor` VARCHAR (50) NULL,'\
    '`numeroCasa_vendedor` VARCHAR(45) NULL,'\
    '`complemento_vendedor` VARCHAR(45) NULL,'\
    'PRIMARY KEY (`id_vendedor`));',

    'CREATE TABLE IF NOT EXISTS `vendas` ('\
    '`id_venda` INT NOT NULL AUTO_INCREMENT,'\
    '`id_produto` BIGINT NOT NULL,'\
    '`id_vendedor` INT NULL,'\
    '`id_cliente` INT NULL,'\
    '`valor` FLOAT NULL,'\
    '`quantidade` INT NULL,'
    'PRIMARY KEY (`id_venda`),'\
    'INDEX `produto_idx` (`id_produto` ASC) VISIBLE,'\
    'INDEX `vendedor_idx` (`id_vendedor` ASC) VISIBLE,'\
    'INDEX `clientea_idx` (`id_cliente` ASC) VISIBLE,'\
    'CONSTRAINT `produto`'\
    '    FOREIGN KEY (`id_produto`)'\
    '    REFERENCES `produtos` (`id_produto`)'\
    '    ON DELETE NO ACTION'\
    '    ON UPDATE NO ACTION,'\
    'CONSTRAINT `vendedor`'\
    '    FOREIGN KEY (`id_vendedor`)'\
    '    REFERENCES `vendedores` (`id_vendedor`)'\
    '    ON DELETE NO ACTION'\
    '    ON UPDATE NO ACTION,'\
    'CONSTRAINT `clientes`'\
    '    FOREIGN KEY (`id_cliente`)'\
    '    REFERENCES `clientes` (`id_cliente`)'\
    '    ON DELETE NO ACTION'\
    '    ON UPDATE NO ACTION);'\
]

#cria um banco de dados para um novo usuario 
class DataBase:
    def create_database(dbName):
        cnx,cursor = Conexao.Con.fazConexao()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS "+ dbName)
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
        return [cnx,cursor]

#cria as tabelas
class Table:
    def criar_tabela(dbName):
        cnx,cursor = DataBase.create_database(dbName)
        try:
            cursor.execute("USE "+dbName)
            for i in tabelas:
                cursor.execute(i)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

        cursor.close()
        cnx.close()