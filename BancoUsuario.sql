CREATE SCHEMA IF NOT EXISTS  'Usuarios';

USE 'Usuarios';

CREATE TABLE 'user' (
                'id' INTEGER NOT NULL PRIMARY KEY,
                'userName' varchar(50),
                'nomeCompleto' varchar(50),
                'email' varchar(50),
                'senha' varchar(120),
                'fone' varchar(15),
                'nomeBanco' varchar(45));
