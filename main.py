from CRUD import CRUDProdutos as crudP
from CRUD import CRUD_Pessoas as crudPessoa
from CRUD import CRUDVendedor as crudV
from CRUD import CRUDVendas
from CRUD import CRUD_Telefones as tel
import os

#faz operaçoes com os produtos
def produtos():
    while True:
        opcao = int(input('\nescolha um opcao: (1) adicionar produto | (2) atualizar produto ' \
            '(3) remover produto | (4) listar produtos | (5) voltar: '))

        if opcao == 1:
            id = input('id: ')
            desc = input('descricao: ')
            marca = input('marca: ')
            cor = input('cor: ')
            tamanho = input('tamanho: ')
            genero = input('genero(masc = M \ fem = F \ unisex = U): ')
            categoria = input('categoria: ')
            qtd = input('quantidade: ')
            precoCusto = input('preco: ')
            crudP.Crud_Produtos.addProduto(id,desc,marca,cor,tamanho,genero,categoria,qtd,precoCusto)

        elif opcao == 2:
            id = input('id: ')
            desc = input('descricao: ')
            marca = input('marca: ')
            cor = input('cor: ')
            tamanho = input('tamanho: ')
            genero = input('genero(M\\F\\U): ')
            categoria = input('gategoria: ')
            qtd = input('quantidade: ')
            precoCusto = input('preco: ')
            crudP.Crud_Produtos.UpdateProduto(id,desc,marca,cor,tamanho,genero,categoria,qtd,precoCusto,)

        elif opcao == 3:
            id = input('id: ')
            crudP.Crud_Produtos.deleteProduto(id)

        elif opcao == 4:
            crudP.Crud_Produtos.selectProdutos()

        elif opcao == 5:
            return

#faz operacoes com os pessoa
def pessoa():
    while True:
        opcao = int(input('\nescolha um opcao: (1) adicionar pessoa | (2) atualizar pessoa ' \
            '(3) remover pessoa | (4) listar pessoa | (5) listar telefone | (6) voltar: '))

        if opcao == 1:
            nome = input('nome: ')
            cpf = input('cpf: ')
            sexo =  input('sexo: ')
            estado = input('estado (ex: MG): ')
            cidade = input('cidade: ')
            bairro = input('bairro: ')
            rua = input('rua: ')
            numeroCasa = input('numero da Casa: ')
            complemento = input('complemento: ')
            tipo =  input('tipo: ')
            quantidadeTel = int(input('Quantos telefones deseja adicionar? '))
            crudPessoa.CrudPessoa.add_Pessoa(nome,cpf,sexo,estado,cidade,bairro,rua,numeroCasa,complemento,tipo)

            i = 1
            while i <= quantidadeTel:
                telefone = input('{} - numero: '.format(i))
                tel.CrudTelefones.insert_Telefone(cpf,telefone)
                i+=1

        elif opcao == 2:
            cpf = input('cpf: ')
            nome = input('nome: ')
            estado = input('estado (ex: MG): ')
            cidade = input('cidade: ')
            bairro = input('bairro: ')
            rua = input('rua: ')
            numeroCasa = input('numero da Casa: ')
            complemento = input('complemento: ')
            tipo =  input('tipo: ')
            crudPessoa.CrudPessoa.update_Pessoa(cpf,nome,estado,cidade,bairro,rua,numeroCasa,complemento,tipo)
            print('\n')
            tel.CrudTelefones.select_Telefone(cpf)
            op = int(input('\nO que fazer com telefones: (1) alterar | (2) remover | (3) nada: '))
            
            if op == 1:
                qtd = int(input('quantos deseja alterar? '))
                i = 1
                while i <= qtd:
                    telefoneA, telefoneN = input('telefoneAntigo telefoneNovo: ').split()
                    tel.CrudTelefones.update_Telefone(cpf,telefoneN,telefoneA)
                    i+=1

            elif op == 2:
                qtd = int(input('quantos deseja remover? '))
                i = 1
                while i <= qtd:
                    telefoneA = input('telefone: ')
                    tel.CrudTelefones.delete_Telefone(cpf,telefoneA)
                    i+=1
            else:
                pass

        elif opcao == 3:
            cpf = input('cpf: ')
            crudPessoa.CrudPessoa.delete_Pessoa(cpf)

        elif opcao == 4:
            crudPessoa.CrudPessoa.select_Pessoa()

        elif opcao == 5:
            cpf = input('cpf: ')
            tel.CrudTelefones.select_Telefone(cpf)

        elif opcao == 6:
            return

#faz operacoes com os vendedores
def vendedores():
    while True:
        opcao = int(input('\nescolha um opcao: (1) adicionar vendedor | (2) atualizar vendedor ' \
            '(3) listar vendedores | (4) voltar: '))

        if opcao == 1:
            cpf = input('cpf: ')
            salario = input('salario: ')
            data_Admissao = input('data admissao (yy-mm-dd): ')
            data_Demissao = input('data demissao (yy-mm-dd): ')
            crudV.Crud_vendedores.add_vendedor(cpf,salario,data_Admissao,data_Demissao)

        elif opcao == 2:
            cpf = input('cpf: ')
            salario = input('salario: ')
            data_Demissao = input('data demissao (yy-mm-dd): ')
            crudV.Crud_vendedores.update_vendedor(cpf,salario,data_Demissao)

        elif opcao == 3:
            crudV.Crud_vendedores.select_vendedores()

        elif opcao == 4:
            return

#faz operacoes com as vendas
def vendas():
    while True:
        opcao = int(input('\nescolha um opcao: (1) adicionar venda |  (2) listar vendas | (3) voltar: '))

        if opcao == 1:
            idP = input('id do produto: ')
            cpfV = input('cpf do vendedor: ')
            cpfC = input('cpf do cliente: ')
            valor = input('valor: ')
            qtd = input('quantidade: ')
            CRUDVendas.Crud_vendas.add_venda(idP,cpfV,cpfC,valor,qtd)

        elif opcao == 2:
            CRUDVendas.Crud_vendas.select_vendas()

        elif opcao == 3:
            return


#main
def main():
    while True:
        opcao = int(input('\nescolha um opcao: (1) produtos | (2) clientes | (3) vendedores | (4) vendas '\
            '| (5) sair:  '))

        if opcao == 1: 
            os.system('cls' if os.name == 'nt' else 'clear')   
            produtos()

        elif opcao == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            pessoa()
        
        elif opcao == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            vendedores()

        elif opcao == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            vendas() 
    
        elif opcao == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            return

main()