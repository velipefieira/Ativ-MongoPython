from connection import database
from datetime import datetime


def cadastrarVendedor():
    nome = input("Insira o nome do vendedor: ")
    cnpj = input("Insira o CNPJ: ")
    data_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    qntVendedores = database.get_node_count('Vendedor')

    idVendedor = qntVendedores + 1

    cadastroQuery = (
        "CREATE (v:Vendedor { id: $id, nome: $nome, cnpj: $cnpj, data_cadastro: $data_cadastro }) RETURN v"
    )

    result = database.query(cadastroQuery, 
        id=idVendedor,
        nome=nome,
        cnpj=cnpj,
        data_cadastro=data_cadastro
    )

    if result:
        print("Vendedor cadastrado!")
    else:
        print("Erro ao cadastrar vendedor.")