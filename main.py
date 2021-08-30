from login import Login
import CRUDProdutos as crudP
import CRUDClientes as crudC
import CRUDVendedor as crudV
import CRUDVendas
import CRUDUser
from usuario import dbDao
import os

#faz operaçoes com os produtos
def produtos(db):
    while True:
        opcao = int(input('escolha um opcao: (1) adicionar produto | (2) atualizar produto ' \
            '(3) remover produto | (4) listar produtos | (5) voltar: '))

        if opcao == 1:
            id = input('id: ')
            desc = input('descricao: ')
            marca = input('marca: ')
            cor = input('cor: ')
            tamanho = input('tamanho: ')
            genero = input('genero(masc = 0 \ fem = 1): ')
            categoria = input('gategoria: ')
            qtd = input('quantidade: ')
            precoCusto = input('preco: ')
            crudP.Crud_Produtos.addProduto(db,id,desc,marca,cor,tamanho,genero,categoria,qtd,precoCusto)

        elif opcao == 2:
            id = input('id: ')
            desc = input('descricao: ')
            marca = input('marca: ')
            cor = input('cor: ')
            tamanho = input('tamanho: ')
            genero = input('genero(M\F\U): ')
            categoria = input('gategoria: ')
            qtd = input('quantidade: ')
            precoCusto = input('preco: ')
            crudP.Crud_Produtos.UpdateProduto(db,id,desc,marca,cor,tamanho,genero,categoria,qtd,precoCusto)

        elif opcao == 3:
            id = input('id: ')
            crudP.Crud_Produtos.deleteProduto(db,id)

        elif opcao == 4:
            crudP.Crud_Produtos.selectProdutos(db)

        elif opcao == 5:
            return

#faz operacoes com os clientes
def clientes(db):
    while True:
        opcao = int(input('escolha um opcao: (1) adicionar cliente | (2) atualizar cliente ' \
            '(3) remover cliente | (4) listar clientes | (5) voltar: '))

        if opcao == 1:
            nome = input('nome: ')
            cpf = input('cpf: ')
            telefone = input('telefone: ')
            estado = input('estado (ex: MG): ')
            cidade = input('cidade: ')
            bairro = input('bairro: ')
            rua = input('rua: ')
            numeroCasa = input('numero da Casa: ')
            complemento = input('complemento: ')
            crudC.Crud_clientes.add_cliente(db,nome,cpf,telefone,estado,cidade,bairro,rua,numeroCasa,complemento)

        elif opcao == 2:
            id = input('id: ')
            nome = input('nome: ')
            telefone = input('telefone: ')
            estado = input('estado (ex: MG): ')
            cidade = input('cidade: ')
            bairro = input('bairro: ')
            rua = input('rua: ')
            numeroCasa = input('numero da Casa: ')
            complemento = input('complemento: ')
            crudC.Crud_clientes.update_cliente(db,id,nome,telefone,estado,cidade,bairro,rua,numeroCasa,complemento)

        elif opcao == 3:
            id = input('id: ')
            crudC.Crud_clientes.delete_cliente(db,id)

        elif opcao == 4:
            crudC.Crud_clientes.select_clientes(db)

        elif opcao == 5:
            return

#faz operacoes com os vendedores
def vendedores(db):
    while True:
        opcao = int(input('escolha um opcao: (1) adicionar vendedor | (2) atualizar vendedor ' \
            '(3) remover vendedor | (4) listar vendedores | (5) voltar: '))

        if opcao == 1:
            nome = input('nome: ')
            cpf = input('cpf: ')
            telefone = input('telefone: ')
            salario = input('salario: ')
            data_Admissao = input('data admissao (yy-mm-dd): ')
            data_Demissao = input('data demissao (yy-mm-dd): ')
            estado = input('estado (ex: MG): ')
            cidade = input('cidade: ')
            bairro = input('bairro: ')
            rua = input('rua: ')
            numeroCasa = input('numero da Casa: ')
            complemento = input('complemento: ')
            crudV.Crud_vendedores.add_vendedor(db,nome,cpf,telefone,salario,data_Admissao,data_Demissao,estado,cidade,bairro,rua,numeroCasa,complemento)

        elif opcao == 2:
            nome = input('nome: ')
            telefone = input('telefone: ')
            salario = input('salario: ')
            data_Demissao = input('data demissao (yy-mm-dd): ')
            estado = input('estado (ex: MG): ')
            cidade = input('cidade: ')
            bairro = input('bairro: ')
            rua = input('rua: ')
            numeroCasa = input('numero da Casa: ')
            complemento = input('complemento: ')
            crudV.Crud_vendedores.update_vendedor(db,id,nome,telefone,salario,data_Demissao,estado,cidade,bairro,rua,numeroCasa,complemento)

        elif opcao == 3:
            id = input('id: ')
            crudV.Crud_vendedores.delete_vendedor(db,id)

        elif opcao == 4:
            crudV.Crud_vendedores.select_vendedores(db)

        elif opcao == 5:
            return

#faz operacoes com as vendas
def vendas(db):
    while True:
        opcao = int(input('escolha um opcao: (1) adicionar venda |  (2) listar vendas | (3) voltar: '))

        if opcao == 1:
            idP = input('id do produto: ')
            idV = input('id do vendedor: ')
            idC = input('id do cliente: ')
            valor = input('valor: ')
            qtd = input('quantidade: ')
            CRUDVendas.Crud_vendas.add_venda(db,idP,idV,idC,valor,qtd)

        elif opcao == 2:
            CRUDVendas.Crud_vendas.select_vendas(db)

        elif opcao == 3:
            return

#faz operacoes com o usuario
def usuario(db):
    while True:
        opcao = int(input('escolha um opcao:  (1) atualizar usuario | (2) remover usuario | (3) voltar: '))

        if opcao == 1:
            nome = input('nome completo: ')
            senha = input('nova senha: ')
            email = input('email: ')
            telefone = input('telefone: ')
            idUser,x = dbDao.select()
            CRUDUser.Crud_usuario.UpdateUser(nome,senha,email,telefone,idUser)
        
        elif opcao == 2:
            idUser,x = dbDao.select()
            CRUDUser.Crud_usuario.DeleteUser(idUser)
            exit(0)

        elif opcao == 4:
            x,y=dbDao.select()
            print(y)
        
        elif opcao == 3:
            return

#faz operacoes de cadastro de usuario
def cadastrar():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        userName = input('userName: ')
        nomeCompleto = input('nome completo: ')
        senha = input('sennha: ')
        email = input('email: ')
        telefone = input('telefone: ')
        bool = CRUDUser.Crud_usuario.addUser(userName,nomeCompleto,senha,email,telefone)
        if bool : break
    
    logar()
    return bool

#faz o login
def logar():
    cont = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        user = input('insira o nome do usuario ou email: ')
        senha = input('insira a senha: ')

        boo,x = Login.logar(user,senha)

        if not boo  and x == 1:
            cont += 1

            if x == 1 and boo == False and cont == 3:
                opcao2 = input('deseja redefinir sua senha? (s/n): ')
                if opcao2 == 's':
                    email = input('digite o email cadastrado: ')
                    Login.esqueceuSenha(email)
                    cont = 0

        elif boo:
            db = dbDao.nomeBanco()
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                opcao = int(input('escolha um opcao: (1) produtos | (2) clientes | (3) vendedores | (4) vendas '\
                        '| (5) usuario | (6) sair:  '))

                    
                if opcao == 1: 
                    os.system('cls' if os.name == 'nt' else 'clear')   
                    produtos(db)

                elif opcao == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    clientes(db)
                
                elif opcao == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    vendedores(db)

                elif opcao == 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    vendas(db) 

                elif opcao == 5:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    usuario(db)  
                
                elif opcao == 6:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return True

#main
def exe():
    opcao = int(input('escolha uma opcao: (1) Logar | (2) Cadastrar \n'))
    if opcao == 1:
        boo = logar()
        return boo
    elif opcao == 2:
        boo = cadastrar()
        return boo
    else:
        print('opcao invalida')

boo = exe()
if boo : dbDao.exclui()